from player import RandomPlayer, NNPlayer
from game import Game
from board import Board
import time


player = NNPlayer("nn1", './models/model.tf')
p2 = RandomPlayer("r1")

nn_win = 0
draw = 0
random_win = 100
game_number = 0

while random_win > 0:

    for i in range(100):
        game_number += 1
        print("game #", game_number)
        board = Board(0, 0)
        player.set_is_training(True)
        g = Game(board, player, player)
        result = g.play()
        player.train(result)

    draw = 0
    random_win = 0
    nn_win = 0

    for i in range(50):
        player.set_is_training(False)
        if i % 2 == 0:
            board = Board(0, 0)
            g = Game(board, player, p2)
            result = g.play()

            if result == 0:
                draw += 1
            elif result == 1:
                nn_win += 1
            else:
                random_win += 1
        else:
            board = Board(0, 0)
            g = Game(board, p2, player)

            result = g.play()

            if result == 0:
                draw += 1
            elif result == 1:
                random_win += 1
            else:
                nn_win += 1
        if random_win >= 5:
            break
    print(nn_win, draw, random_win)
    time.sleep(2)
