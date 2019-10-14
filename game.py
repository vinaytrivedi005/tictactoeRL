class Game:
    def __init__(self, board, player_x, player_o):
        self.board = board
        self.player_x = player_x
        self.player_o = player_o
        self.turn = 'X'

    def play(self):
        while self.board.evaluate() == 2:
            if self.turn == 'X':
                self.board.insert_x(self.player_x.get_move(self))
                self.turn = 'O'
            elif self.turn == 'O':
                self.board.insert_o(self.player_o.get_move(self))
                self.turn = 'X'

        return self.board.evaluate()

    def get_board(self):
        return self.board
