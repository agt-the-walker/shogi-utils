#!/usr/bin/env python3

import json
import sys

import pexpect
from shogi import Board, CSA

ENGINE_DIR = '/usr/local/opt/elmo.sdt5'
ENGINE_NAME = 'YaneuraOu-by-gcc'

OPTIONS = {
    'Hash': 16 * 1024,  # I.e. 16 Gb. I have 32 Gb of RAM

    # thanks https://linuxfan.info/elmo-sdt5-on-linux
    'BookDepthLimit': 0,
    'BookMoves': 200,
    'ConsiderBookMoveCount': True,
    'NetworkDelay': 0,
    'NetworkDelay2': 0,
}

MIN_DEPTH = 21


def parse_game(f):
    csa_lines = []
    for line in json.load(f)['contents'].splitlines():
        if line[0] == 'I' or line[0] == '#':
            continue
        elif line.startswith("'ILLEGAL_MOVE"):
            del csa_lines[-2:]
            continue
        csa_lines.append(line)

    return CSA.Parser.parse_str("\n".join(csa_lines))[0]


def analyze_game(game):
    child = pexpect.spawn(ENGINE_NAME, cwd=ENGINE_DIR)
    child.sendline('usi')
    child.expect('usiok')
    for key, value in OPTIONS.items():
        child.sendline('setoption name {} value {}'.format(key, value))
    child.sendline('isready')
    child.expect('readyok')

    board = Board(game['sfen'])
    for move in game['moves']:
        board.push_usi(move)
        print(move)

        child.sendline('position sfen {}'.format(board.sfen()))
        child.sendline('go depth {}'.format(MIN_DEPTH))

        info_line = ''
        while True:
            line = child.readline().decode().rstrip()
            if line.startswith('info'):
                info_line = line
            elif line.startswith('bestmove '):
                print(info_line)
                print(line)
                print()
                break


def main():
    game = parse_game(sys.stdin)
    analyze_game(game)


if __name__ == '__main__':
    main()
