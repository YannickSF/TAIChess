

class Player:
    def __init__(self, username, color):
        self.username = username
        self.color = color

    def brain(self):
        pass

    def play(self):
        # use input or brain(strategy)
        print(self.username + "Play : ")
        return None

    def __repr__(self):
        return {'username': self.username, 'color': self.color}

    def __str__(self):
        return self.__repr__().__str__()
