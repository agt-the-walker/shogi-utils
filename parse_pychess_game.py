#!/usr/bin/env python3

import re
import shogi
import sys
from shogi import CSA


FEN_INIT = 'lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL[-] w 0 1'


def fix_column(column):
    return str(9 + ord('a') - ord(column))


def fix_row(row):
    return chr(9 + ord('a') - int(row))


def fix_square(square):
    return fix_column(square[0]) + fix_row(square[1])


def fix_piece(piece):
    # thanks https://github.com/fairy-stockfish/Fairy-Stockfish
    if piece == 'D':  # DRAGON
        return '+R'
    elif piece == 'H':  # DRAGON_HORSE
        return '+B'

    return piece


def parse_move(board, move):
    if m := re.match(r'([A-Z])\@(\w{2})', move):  # drop
        return shogi.Move.from_usi(fix_piece(m[1]) + '*' + fix_square(m[2]))
    elif m := re.match(r'([A-Z])x?([a-i])?([1-9])?(\w{2})(=?)',
                       move):  # move/capture
        piece = fix_piece(m[1])
        return parse_abbreviated_move_components(
                board,
                shogi.Piece.from_symbol(
                    piece if board.turn == shogi.BLACK else piece.lower()),
                fix_column(m[2]) if m[2] else None,
                fix_row(m[3]) if m[3] else None,
                fix_square(m[4]),
                m[5] == '=')

    sys.exit('Unexpected move: {}'.format(move))


def parse_abbreviated_move_components(board, piece, from_column, from_row,
                                      to_square, promotion):
    for move in board.legal_moves:
        if board.piece_at(move.from_square) == piece and \
           (not from_column or
            shogi.SQUARE_NAMES[move.from_square][0] == from_column) and \
           (not from_row or
            shogi.SQUARE_NAMES[move.from_square][1] == from_row) and \
           shogi.SQUARE_NAMES[move.to_square] == to_square and \
           move.promotion == promotion:
            return move

    sys.exit('No legal move with piece type {} from column {} and row {} '
             'to square {} and promotion {}'.
             format(piece, from_column, from_row, to_square, promotion))


def main():
    csa_moves = []
    board = shogi.Board()

    for line in sys.stdin:
        if m := re.match(r'\[White "(.+?)"\]', line):
            print('N' + CSA.COLOR_SYMBOLS[0] + m[1])
        elif m := re.match(r'\[Black "(.+?)"\]', line):
            print('N' + CSA.COLOR_SYMBOLS[1] + m[1])
        elif m := re.match(r'\[FEN "(.+?)"\]', line):
            fen = m[1]
            if fen != FEN_INIT:
                sys.exit('Unexpected FEN: {}', fen)
        elif line.startswith('1'):
            for token in re.findall(r'[A-Z]\S+', line):
                move = parse_move(board, token)
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

    print('PI')
    print('+')
    for csa_move in csa_moves:
        print(csa_move)


if __name__ == '__main__':
    main()
