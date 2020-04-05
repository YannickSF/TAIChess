
from board.board import ChessBoard
from board.player import Player


def main():
    b = ChessBoard()

    p1 = Player('y', 'RED')
    p2 = Player('S', 'BLACK')
    b.set_player(p1, p2)

    b.initialize()
    for i in range(len(b.board)):
        print(b.board[i])


if __name__ == '__main__':
    main()
