
from game.engine import Engine


class AI(Engine):
    def __init__(self, name=None, color='WHITE'):
        Engine.__init__(self)
        self.name = name
        self.color = color

    def brain(self):
        pass

    """ return de pair of coord to moov a piece """
    def play(self):
        # score = self._evaluate_score()
        # values = self.brain()
        print("AI Play : ")
        return None

    def __repr__(self):
        return {'name': self.name, 'color': self.color}

    def __str__(self):
        return self.__repr__().__str__()
