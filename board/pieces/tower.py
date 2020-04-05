
from board.object import Pieces


class Tower(Pieces):
    def __init__(self, x=0, y=0, color=None):
        Pieces.__init__(self, x, y, color, 'Tower')
        self.value = 5
