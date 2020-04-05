

class Pieces:

    def __init__(self, x='', y=0, color=None, stype=None):
        self.color = color
        self.x = x
        self.y = y
        self.type = stype
        self.value = 0

    def been_pwnd(self):
        self.x = 'z'
        self.y = -1

    def __repr__(self):
        return {'x': self.x, 'y': self.y, 'color': self.color, 'type': self.type, 'value': self.value}.__str__()

    def __str__(self):
        return self.__repr__().__str__()
