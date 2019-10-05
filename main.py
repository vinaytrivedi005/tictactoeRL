from player import RandomPlayer, NNPlayer
from game import Game
import sys


player = NNPlayer("nn")
p2 = RandomPlayer("r1")
print(sys.argv[1])
if sys.argv[1] == "train":

    nn_win = 0
    draw = 0
    random_win = 100

    while random_win > 0:

        for i in range(100):
            g = Game(player, player)
            result = g.play()
            player.train(result)

        draw = 0
        random_win = 0
        nn_win = 0

        for i in range(100):
            if i % 2 == 0:
                g = Game(player, p2)
                result = g.play()

                if result == 0:
                    draw += 1
                elif result == 1:
                    nn_win += 1
                else:
                    random_win += 1
                    break
            else:
                g = Game(p2, player)

                result = g.play()

                if result == 0:
                    draw += 1
                elif result == 1:
                    random_win += 1
                    break
                else:
                    nn_win += 1
        print(nn_win, draw, random_win)
