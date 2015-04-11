# Purpose

## shuffle-first-row

This program prints Shogi22680 positions with optional restrictions.


# Requirements

* [Boost Program Options](http://www.boost.org/doc/libs/1_57_0/doc/html/program_options.html)
* [GNU Compiler Collection (GCC)](http://www.gnu.org/software/gcc/), recent 
  enough to support C++11
* [GNU Make](http://www.gnu.org/software/make/)


# Usage

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


# Credits

* http://www.shogi.net/shogi-l/Archive/2007/Nmar16-03.txt: introduced
  Shogi22680
* http://en.wikipedia.org/wiki/Capablanca_random_chess: one of the rules is
  "All pawns must be protected in initial setup", which provided inspiration
  for the `--protect` and `--protect-more` options.
