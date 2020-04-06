
from game.pieces.object import Pieces


class King(Pieces):
    def __init__(self, x=0, y=0, color=None):
        Pieces.__init__(self, x, y, color, 'King')
        self.value = 0
