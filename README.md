[![Build Status](https://travis-ci.org/agt-the-walker/shogi-utils.svg?branch=master)](https://travis-ci.org/agt-the-walker/shogi-utils)


# Preamble

I like Shogi, but I also like other abstracts such as Arimaa and especially
[Capablanca Random Chess](http://brainking.com/en/GameRules?tp=75), since I
hate studying openings. For this reason, I'd like to try Shogi22680, but I'm
also interested in [other board sizes and pieces](cheatsheet.md).

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
random piece in the first row (except the King, obviously) by a random
one introduced in Okisaki Shogi, then we get 33 * 8 * 3 = 792 different
starting positions.

Another option to get more starting positions would be to add a piece, either
placed midway between the bishop and the rook, or in hand, to be introduced
whenever the player moves a piece in the first row from its starting position,
like in [Seirawan Chess](https://en.wikipedia.org/wiki/Seirawan_chess). For
instance, if we swap two pieces in the first row then add a random one
introduced in Wa Shogi, then we get 33 * 15 = 495 different starting positions.

Adding new pieces is not without consequences. Firstly, the Jishogi rule should
probably be replaced by the Try rule, where another way to win would be to
bring one's King to the original square of the opponent's King (if this square
is not controlled by enemy pieces). In any case, the Jishogi rule looks rather
artificial to me, whereas the Try rule works with other board sizes and/or
pieces. Secondly, it might be advisable to restrict drops if too many/powerful
pieces are in play compared to standard Shogi. There are several ways to do so:

1. a non-pawn drop cannot checkmate
2. a drop cannot check
3. a drop cannot attack enemy pieces (including the King, excluding pawns)
4. a drop cannot attack enemy pieces (including the King) or pawns


# Utilities

## Purpose

### shuffle-first-row

This program prints Shogi22680 positions with optional restrictions. K = King,
N = Knight, etc.


## Requirements

* [Boost Program Options](http://www.boost.org/doc/libs/1_57_0/doc/html/program_options.html)
* [GNU Compiler Collection (GCC)](http://www.gnu.org/software/gcc/), recent 
  enough to support C++11
* [GNU Make](http://www.gnu.org/software/make/)


## Usage

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
