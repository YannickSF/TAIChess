
from board.object import Pieces


class Knight(Pieces):
    def __init__(self, x=0, y=0, color=None):
        Pieces.__init__(self, x, y, color, 'Knight')
        self.value = 3
