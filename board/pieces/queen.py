
from board.object import Pieces


class Queen(Pieces):
    def __init__(self, x=0, y=0, color=None):
        Pieces.__init__(self, x, y, color, 'Queen')
        self.value = 9
