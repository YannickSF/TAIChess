
import time
from game.board import ChessBoard
from players.player import Player
from players.ai import AI


def print_board(b):
    for i in range(len(b.board)):
        print(b.board[i])


def party(player_one, player_two):
    b = ChessBoard()
    b.set_player(player_one, player_two)

    print('==== INITIALIZE =====')
    b.initialize()
    print_board(b)

    starter = True
    if b.bot_side == b.player2.color:
        starter = False

    loop = 0
    print("===START===")

    while not b.is_game_end():
        print("LOOP => " + loop)
        if starter:
            b.player1.play()
            b.player2.play()
        else:
            b.player2.play()
            b.player1.play()

        loop += 1
        print_board(b)
        print('==============================')

    return None


def console():
    print("Choose opponent : ")
    p1 = Player('y', 'RED')
    ai = AI('sylys')
    party(p1, ai)


if __name__ == '__main__':
    console()
