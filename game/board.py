
from .pieces.object import Pieces
from .pieces.king import King
from .pieces.queen import Queen
from .pieces.knight import Knight
from .pieces.fool import Fool
from .pieces.tower import Tower
from .pieces.pawn import Pawn

from .engine import Engine


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


class ChessBoard:
    def __init__(self):
        self._limit_x = self._limit_y = 8
        self.board = [i for i in range(self._limit_x * self._limit_y)]

        self.player1 = None
        self.player2 = None

        self.top_side = None
        self.bot_side = None

        self._e = Engine(self)

    @staticmethod
    def _init_guard(x, y, color):
        guard = {'a': Tower(x, y, color),
                 'b': Knight(x, y, color),
                 'c': Fool(x, y, color),
                 'd': Queen(x, y, color),
                 'e': King(x, y, color),
                 'f': Fool(x, y, color),
                 'g': Knight(x, y, color),
                 'h': Tower(x, y, color)}
        return guard[x]

    def set_player(self, player_one, player_two):
        if player_one is not None:
            self.player1 = player_one

        if player_two is not None:
            self.player2 = player_two

    def initialize(self):
        if self.player1 is None or self.player2 is None:
            print('Need two players !')
            return None

        color = self.player1.color
        self.top_side = color
        for i in range(len(self.board)):
            if i > len(self.board) / 2:
                color = self.player2.color
                self.bot_side = color

            if '1' in _COORD[i] or '8' in _COORD[i]:
                self.board[i] = self._init_guard(_COORD[i][:1], _COORD[i][1:], color)

            if '2' in _COORD[i] or '7' in _COORD[i]:
                self.board[i] = Pawn(_COORD[i][:1], _COORD[i][1:], color)

        # print(self.top_side)
        # print(self.bot_side)

    def get_piece_by_coord(self, coord):
        return self.board[_COORD.index(coord)]

    def get_piece_by_value(self, value):
        return self.board[value]

    def moov(self, origin, to):
        orval = _COORD.index(origin)
        toval = _COORD.index(to)

        p = self.board[orval]
        p.x = to[:1]
        p.y = to[1:]

        if p.type == 'Pawn':
            p.is_1st_moov = False

        self.board[orval] = orval
        self.board[toval] = p

    def is_game_end(self):
        for p in range(len(self.board)):
            if self.board[p] is Pieces and self.board[p].type == 'King':
                sts = self._e.compute_moovements(self.board[p])
                if len(sts) > 0:
                    return True
                else:
                    return False
