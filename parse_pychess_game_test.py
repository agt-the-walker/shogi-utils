#!/usr/bin/env python3

from parse_pychess_game import fix_square


def test_fix_square():
    assert fix_square('h4') == '2f'
