#!/usr/bin/env python3

import argparse
import configparser
import os
from pathlib import PosixPath
import sys
from urllib.parse import urlparse

import mechanicalsoup
import requests

CONFIG_FILE = PosixPath('~/.fetch-81dojo-games.cfg').expanduser()

PLAYER_URL = 'https://system.81dojo.com/en/players/show/{}'
HOST = urlparse(PLAYER_URL).hostname
LOGIN_URL = 'https://system.81dojo.com/en/players/sign_in'
SEARCH_URL = 'https://system.81dojo.com/en/kifus/search/form'
REFERER_URL = 'https://81dojo.com'
KIFU_URL = 'https://system.81dojo.com/api/v2/kifus/{}.json'


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help='Directory used to store games')
    args = parser.parse_args()

    if not os.path.isdir(args.dir):
        sys.exit(args.dir + ' is not a directory')
    return args.dir


def get_user_password():
    import netrc
    netrc = netrc.netrc()
    info = netrc.authenticators(HOST)
    if info is None:
        sys.exit('~/.netrc should include: machine #{HOST} login [...] '
                 'password [...]')
    return info[0], info[2]


def get_config(user):
    config = configparser.RawConfigParser()
    config.read(CONFIG_FILE)

    if user not in config.sections():
        config[user] = {}
        config[user]['stats'] = ''
        config[user]['latest_game_id'] = ''

    return config


def fetch_stats(browser, user, user_config):
    browser.open(PLAYER_URL.format(user))
    page = browser.get_current_page()
    current_stats = page.find(string='Games').find_next('td').contents[0]\
                        .strip()

    if current_stats == user_config['stats']:
        sys.exit('No game since last run')
    user_config['stats'] = current_stats


def log_in(browser, user, password):
    browser.open(LOGIN_URL)
    browser.select_form()
    browser['player[name]'] = user
    browser['player[password]'] = password
    browser.submit_selected()


def get_game_ids(browser, user_config):
    oldest_date = None
    game_ids = set()

    while True:
        browser.open(SEARCH_URL)
        browser.select_form()
        browser['conditions[search_from]'] = '1970-01-01'  # Unix Epoch
        if oldest_date:
            print('Limit reached. Also searching games until ' + oldest_date)
            browser['conditions[search_until]'] = oldest_date
        else:
            print('Searching all games')
        browser.submit_selected()

        page = browser.get_current_page()
        for row in page.find('table', class_='list').find_all('tr'):
            cells = row.find_all('td')
            if cells:
                oldest_date = next(cells[1].children)
                game_id = os.path.basename(cells[-1].find('a')['href'])

                if game_id == user_config['latest_game_id']:
                    return game_ids

                game_ids.add(int(game_id))

        if not page.find(
                string='Number of matching kifus reached your limit.'):
            break

    return game_ids


def save_games(game_ids, game_dir, user_config):
    with requests.Session() as session:
        session.headers.update({'Referer': REFERER_URL})
        for game_id in sorted(game_ids):
            print('Saving game {}'.format(game_id))

            kifu_url = KIFU_URL.format(game_id)
            with open(os.path.join(game_dir, os.path.basename(kifu_url)),
                      'w') as f:
                f.write(session.get(kifu_url).text + '\n')

    user_config['latest_game_id'] = str(max(game_ids))


def save_config(config):
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)


def main():
    game_dir = parse_arguments()
    user, password = get_user_password()
    config = get_config(user)

    browser = mechanicalsoup.StatefulBrowser()
    fetch_stats(browser, user, config[user])
    log_in(browser, user, password)
    game_ids = get_game_ids(browser, config[user])
    browser.close()

    save_games(game_ids, game_dir, config[user])
    save_config(config)


if __name__ == '__main__':
    main()
