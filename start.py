
from game.board import ChessBoard
from players.player import Player
from game.engine import Engine


def party_pvp():
    b = ChessBoard()
    p1 = Player('y', 'RED')
    p2 = Player('s', 'BLACK')

    b.set_player(p1, p2)
    b.initialize()

    for i in range(len(b.board)):
        print(b.board[i])


def party_pvm():
    b = ChessBoard()

    p1 = Player('y', 'RED')
    e = Engine()  # WHITE by default

    b.set_player(p1, e)
    b.initialize()
    e.current_board = b

    for i in range(len(b.board)):
        print(b.board[i])

    # print(e.compute_moovements(b.get_piece_by_coord('d4')))


def console():
    pass


if __name__ == '__main__':
    console()
