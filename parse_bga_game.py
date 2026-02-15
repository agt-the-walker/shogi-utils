#!/usr/bin/env python3

import re
import shogi
import sys
from lxml import html
from shogi import CSA


def fix_square(square):
    return square[0] + chr(ord('a') + int(square[1])-1)


def parse_move(board, move):
    m = re.match(r'([A-Z]\*)(\d{2})', move)
    if m:  # drop
        return shogi.Move.from_usi(m[1] + fix_square(m[2]))

    m = re.match(r'(\+?[A-Z])(\d{2})?[-x](\d{2})(\+?)', move)
    if m:  # move/capture
        if m[2]:  # long notation
            return shogi.Move.from_usi(fix_square(m[2]) + fix_square(m[3]) +
                                       m[4])
        else:     # abbreviated notation
            return parse_abbreviated_move_components(
                    board,
                    shogi.Piece.from_symbol(
                        m[1] if board.turn == shogi.BLACK else m[1].lower()),
                    fix_square(m[3]),
                    m[4] == '+')

    sys.exit('Unexpected move: {}'.format(move))


def parse_abbreviated_move_components(board, piece, to_square, promotion):
    for move in board.legal_moves:
        if board.piece_at(move.from_square) == piece and \
           shogi.SQUARE_NAMES[move.to_square] == to_square and \
           move.promotion == promotion:
            return move

    sys.exit('No legal move with piece type {} to square {} and promotion {}'.
             format(piece, to_square, promotion))


def main():
    csa_moves = []
    resignation = False

    tree = html.parse(sys.stdin)
    board = shogi.Board()
    num_players_seen = 0
    for div in tree.xpath('//div[contains(@class, "gamelogreview")]'):
        m = re.match(r'(.+) plays (\S+)', div.text)
        if m:
            if num_players_seen < 2:
                print('N' + CSA.COLOR_SYMBOLS[num_players_seen] + m[1])
                num_players_seen += 1

            move = parse_move(board, m[2])
            turn = board.turn
            board.push(move)

            if move.from_square is None:
                from_square = '00'
                piece_type = move.drop_piece_type
            else:
                from_square = CSA.SQUARE_NAMES[move.from_square]
                piece_type = board.piece_at(move.to_square).piece_type
            csa_moves.append(CSA.COLOR_SYMBOLS[turn] +
                             from_square +
                             CSA.SQUARE_NAMES[move.to_square] +
                             CSA.PIECE_SYMBOLS[piece_type])

        elif div.text.endswith(' resigned'):
            resignation = True
            break

    print('PI')
    print('+')
    for csa_move in csa_moves:
        print(csa_move)
    if resignation:
        print('%TORYO')


if __name__ == '__main__':
    main()
