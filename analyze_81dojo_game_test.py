#!/usr/bin/env python3

import json

from analyze_81dojo_game import parse_game

def test_parse_game():
    parse_game(open("4471112.json"))
