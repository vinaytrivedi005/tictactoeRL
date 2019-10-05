from board import Board


class Game:
    def __init__(self, player_x, player_o):
        self.board = Board()
        self.player_x = player_x
        self.player_o = player_o
        self.turn = 0

    def play(self):
        while self.board.evaluate() == 2:
            if self.turn == 0:
                self.board.insert_x(self.player_x.get_move(self.board, self.turn))
                self.turn = 1
            elif self.turn == 1:
                self.board.insert_o(self.player_o.get_move(self.board, self.turn))
                self.turn = 0
        # print("")
        # print(self.board.get_classic_board())
        # print("")

        return self.board.evaluate()
