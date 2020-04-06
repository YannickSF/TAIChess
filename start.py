
from game.board import ChessBoard
from game.player import Player
from game.engine import Engine


def main():
    b = ChessBoard()

    p1 = Player('y', 'RED')
    p2 = Player('e', 'BLACK')
    e = Engine()

    b.set_player(p1, e)
    b.initialize()
    e.current_board = b

    b.moov('d8', 'd4')
    for i in range(len(b.board)):
        print(b.board[i])

    print(e.compute_moovements(b.get_piece_by_coord('d4')))


if __name__ == '__main__':
    main()
