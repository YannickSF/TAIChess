
from game.pieces.object import Pieces
from game.pieces.king import King
from game.pieces.queen import Queen
from game.pieces.knight import Knight
from game.pieces.fool import Fool
from game.pieces.tower import Tower
from game.pieces.pawn import Pawn


_COORD = [
    'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
    'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
    'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
    'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
    'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
    'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
    'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
    'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1',
    ]

_BOARD_LIMITED = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                  -1,  0,  1,  2,  3,  4,  5,  6,  7, -1,
                  -1,  8,  9, 10, 11, 12, 13, 14, 15, -1,
                  -1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
                  -1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
                  -1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
                  -1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
                  -1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
                  -1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
                  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]


VECTOR_N = -8
VECTOR_NE = -7
VECTOR_E = 1
VECTOR_SE = 9
VECTOR_S = 8
VECTOR_SW = 7
VECTOR_W = -1
VECTOR_NW = -9

KN = VECTOR_N * 2
KE = VECTOR_E * 2
KS = VECTOR_S * 2
KW = VECTOR_W * 2


class Engine:
    def __init__(self, board=None):
        self.current_board = board

    @staticmethod
    def get_coord_position(position):
        return _COORD.index(position)

    @staticmethod
    def get_board_position(x):
        return _BOARD_LIMITED.index(x)

    def is_border(self, position):
        if position < 0 or position > 63 or self.get_board_position(position) == -1:
            return True
        return False

    def is_piece(self, value):
        is_piece = self.current_board.get_piece_by_value(value)
        if is_piece.__class__ in [King, Queen, Knight, Fool, Tower, Pawn]:
            return True
        return False

    @staticmethod
    def is_enemy(piece_to_try, piece):
        if piece_to_try.color != piece.color:
            return True
        return False

    def compute_vector(self, x, vector, p=1, piece=None):
        res = []
        find_piece = False
        x = self.get_coord_position(x)

        if p != 1:
            for i in range(1, p):
                if not self.is_border((x + (vector * i))):
                    if find_piece:
                        break

                    if not self.is_piece(x + (vector * i)):
                        res.append(x + (vector * i))
                    else:
                        piece_to_try = self.current_board.get_piece_by_value(x + (vector * i))
                        if self.is_enemy(piece_to_try, piece):
                            res.append(x + (vector * i))
        else:
            for i in range(p):
                if not self.is_border(x + vector):
                    if find_piece:
                        break

                    if not self.is_piece(x + (vector * i)):
                        res.append(x + vector)
                    else:
                        piece_to_try = self.current_board.get_piece_by_value(x + (vector * i))
                        if self.is_enemy(piece_to_try, piece):
                            res.append(x + (vector * i))
                            find_piece = True
        return res

    def compute_vector_to(self, x, vector, p, piece=None):
        x = self.get_coord_position(x)

        if not self.is_border(x + (vector * p)):
            if not self.is_piece(x + (vector * p)):
                return x + (vector * p)
            else:
                piece_to_try = self.current_board.get_piece_by_value(x + (vector * p))
                if self.is_enemy(piece_to_try, piece):
                    return x + (vector * p)
        return None

    def compute_moovements(self, piece):
        p = 1
        vector = []
        possibilities = []

        if piece.type == 'King':
            vector = [VECTOR_N, VECTOR_NE, VECTOR_E, VECTOR_SE, VECTOR_S, VECTOR_SW, VECTOR_W, VECTOR_NW]

        if piece.type == 'Queen':
            p = 8
            vector = [VECTOR_N, VECTOR_NE, VECTOR_E, VECTOR_SE, VECTOR_S, VECTOR_SW, VECTOR_W, VECTOR_NW]

        if piece.type == 'Fool':
            p = 8
            vector = [VECTOR_NE, VECTOR_SE, VECTOR_SW, VECTOR_NW]

        if piece.type == 'Tower':
            p = 8
            vector = [VECTOR_N, VECTOR_E, VECTOR_S, VECTOR_W]

        if piece.type == 'Knight':
            vector = [KN + VECTOR_W, KN + VECTOR_E,
                      KE + VECTOR_N, KE + VECTOR_S,
                      KS + VECTOR_W, KS + VECTOR_E,
                      KW + VECTOR_N, KW + VECTOR_S]

        if piece.type == 'Pawn':
            if piece.colors == self.current_board.top_side:
                vec = VECTOR_S
                vector = [VECTOR_SE, VECTOR_SW]
            if piece.colors == self.current_board.bot_side:
                vec = VECTOR_N
                vector = [VECTOR_NE, VECTOR_NW]

            # 1 case
            possibilities += self.compute_vector(piece.x + piece.y, vec, p, piece)
            # 2 eats
            for v in vector:
                value = self.compute_vector(piece.x + piece.y, v, p, piece)
                possibilities += value
            # 1st moov
            if piece.is_1st_moov:
                possibilities += [self.compute_vector_to(piece.x + piece.y, vec, piece)]
            return possibilities

        for v in vector:
            possibilities += self.compute_vector(piece.x + piece.y, v, p, piece)
        return possibilities

    def static_compute_moovements(self, board, piece):
        self.current_board = board
        return self.compute_moovements(piece)

    def is_threat_king(self):
        # permet de savoir si une pièce menace le roi ennemie.
        pass
