[![Build Status](https://travis-ci.org/agt-the-walker/shogi-utils.svg?branch=master)](https://travis-ci.org/agt-the-walker/shogi-utils)


# Table of contents

* [Utilities](#utilities)
* [On Shogi variants](#on-shogi-variants)


# Utilities


## fetch-81dojo-games

This program fetches all [81Dojo](https://81dojo.com/) games played by you.


### Requirements

* [Python](https://www.python.org/) 3.4+
* [MechanicalSoup](https://pypi.org/project/MechanicalSoup/) Python package
* [Requests](https://pypi.org/project/requests/) Python package


### Usage

Please run the following command the first time:

    # replace "Agt" and "hidden" below with your 81Dojo credentials
    $ echo 'machine system.81dojo.com login Agt password hidden' >>~/.netrc

Then:

    $ mkdir -p ~/81Dojo  # adapt accordingly

    $ ./fetch-81dojo-games ~/81Dojo
    Searching all games
    Limit reached. Also searching games until 2018-04-22
    Saving game 2692582
    [...]
    Saving game 3447638

    $ ./fetch-81dojo-games ~/81Dojo
    No game since last run

    # after playing a few games
    $ ./fetch-81dojo-games ~/81Dojo
    Searching all games
    Saving game 3450595
    Saving game 3451125

    $ ls ~/81Dojo
    2692582.json
    [...]
    3451125.json


### Notes

Some information is stored in `~/.fetch-81dojo-games.cfg` to prevent
unnecessary searches, especially considering they do cost
[D-Miles](https://81dojo.com/documents/81Dojo_Mileage).


## shuffle-first-row

This program prints Shogi22680 positions with optional restrictions. K = King,
N = Knight, etc.


### Requirements

* [Boost Program Options](http://www.boost.org/doc/libs/1_57_0/doc/html/program_options.html)
* [GNU Compiler Collection (GCC)](http://www.gnu.org/software/gcc/), recent 
  enough to support C++11
* [GNU Make](http://www.gnu.org/software/make/)


### Usage

    $ cd ~/src/git/shogi-utils  # adapt accordingly

    $ make

    $ ./shuffle-first-row --help
    [shows usage]

    $ ./shuffle-first-row | wc -l
    22680  # not surprisingly

    # restriction: protect all squares on second row
    $ ./shuffle-first-row --protect | wc -l
    15750

    # restriction: do the same without the help of the king
    $ ./shuffle-first-row --protect-more | wc -l
    8262

    # additional restriction: don't put a lance behind pawns most likely
    #  to be pushed during sente's first move
    $ ./shuffle-first-row --protect-more | grep '^..[^L].[^L]..[^L].' | wc -l
    3798

    # the second position is the standard Shogi starting one
    $ ./shuffle-first-row --protect | grep SGKGS
    LLNSGKGSN
    LNSGKGSNL
    NSGKGSNLL

    # shows a few Shogi22680 positions not listed with --protect
    $ diff <(./shuffle-first-row) <(./shuffle-first-row --protect) | \
      grep '^<' | cut -c3- | shuf -n 3
    SGGLKLSNN  # last square of second row is unprotected
    NLSLGKGSN  # first square of second row is unprotected
    SLLNNGSGK  # fourth square of second row is unprotected

    # shows a few Shogi22680 positions not listed with --protect-more
    $ diff <(./shuffle-first-row --protect) \
           <(./shuffle-first-row --protect-more) | \
      grep '^<' | cut -c3- | shuf -n 3
    KNSGLLSNG  # first square of second row is only protected by the king
    LKLSSGNNG  # second square of second row is only protected by the king
    NKLNSGSGL  # first two squares of second row are only protected by the king


## Credits

* http://www.shogi.net/shogi-l/Archive/2007/Nmar16-03.txt: introduced
  Shogi22680
* http://en.wikipedia.org/wiki/Capablanca_random_chess: one of the rules is
  "All pawns must be protected in initial setup", which provided inspiration
  for the `--protect` and `--protect-more` options.


# On Shogi variants


## Article

I like Shogi, but I also like other abstracts such as
[Arimaa](https://en.wikipedia.org/wiki/Arimaa) and especially [Capablanca
Random Chess](http://brainking.com/en/GameRules?tp=75), since I hate studying
openings. For this reason, I'd like to try Shogi22680 (see above), but I'm also
interested in [other board sizes and pieces](cheatsheet.md).

IMHO, a good Shogi variant:

1. shouldn't be more drawish than Chess
2. shouldn't give the first player an advantage greater than in Chess
3. shouldn't require studying opening theory (principles are fine though)
4. shouldn't last more than twice as long as the average Chess game (in plies)
5. shouldn't be more difficult to learn than
   [Wa Shogi](https://en.wikipedia.org/wiki/Wa_shogi)

Any reasonable Shogi variant with drops shouldn't be near as drawish as Chess.
I propose to use the [Pie rule](https://en.wikipedia.org/wiki/Pie_rule) to
address the second point, since randomizing the starting position (third point)
will probably give the first player a greater than usual advantage in some
cases. For the rest, [Chu Shogi](https://en.wikipedia.org/wiki/Chu_shogi) (and
larger board variants) probably takes too long and is also too difficult to
learn.

Let's get back to opening theory. If at the start of a game, each starting
position has 1% (or less) chance of occurring, then we have probably succeeded
in rendering its study pointless. Shogi22680 is an obvious possibility, but
there are others. For instance, swapping the positions of only three pieces in
the first row produces 145 different starting positions (111 with all squares
on second row protected), which is acceptable.

What if we only swap two pieces in the first row? In this case, we only have 33
different starting positions, which is not enough. However if we also replace a
random piece in the first row (except the king, obviously) by a random one
introduced in [Okisaki Shogi](https://en.wikipedia.org/wiki/Okisaki_shogi),
then we get 33 * 8 * 3 = 792 different starting positions.

Using new pieces is not without consequences. Indeed how many points do they
score as far as the [Jishogi](https://en.wikipedia.org/wiki/Shogi#Impasse) rule
is concerned? Therefore this rule should probably be replaced by the [Try
Rule](https://en.wikipedia.org/wiki/Shogi#Amateur_resolutions), where another
way to win would be to bring one's king to the original square of the
opponent's king (if this square is not controlled by enemy pieces).

Moreover we could keep the standard starting position but choose N random
pieces (including pawns, excluding king, rook or bishop) which will promote
differently. For instance, with N=2, assuming they promote to different pieces
(like Chess queen and Chess knight instead of Shogi gold), we get 17 * 16 = 272
"different" starting positions (264 if we want to ensure that at least one
piece of each type promotes as usual).

Finally we could choose a random piece in the first row (except the king,
obviously) which will become a random one introduced in [Wa
Shogi](https://en.wikipedia.org/wiki/Wa_shogi) the first time it is captured.
In that case we get 8 * 15 = 120 "different" starting positions.

## Play by forum

I'd like to try:
* https://boardgamegeek.com/thread/1949202/shogi-random-starting-position-and-pie-rule
* https://boardgamegeek.com/thread/1960024/shogi-random-pieces-promoting-chess-queen-or-knight
* https://boardgamegeek.com/thread/2254276/shogi-random-piece-promoting-something-unusual-ins
* https://boardgamegeek.com/thread/2324959/sho-shogi-game-1-drops-promoted-drunken-elephant-i
* https://boardgamegeek.com/thread/2055552/wa-shogi-game-1

I'm also interested in unusual handicaps:
* https://boardgamegeek.com/thread/2310051/shogi-different-armies

## Personal announcements

* (2020-06-23) I'm looking for Shogi (将棋) players in/around Lausanne
(Switzerland). My level is 5 kyū according to
[81Dojo](https://81dojo.com/en/). I can give/receive handicap, and beginners
are welcome. I speak French, English and Japanese (somewhat). If you're
interested, send me an
[email](mailto:boardgamegeek-user@MY\_GITHUB\_USERNAME.net)!
