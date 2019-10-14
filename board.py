import math


class Board:

    def __init__(self, X, O):
        self.X = int(X)
        self.O = int(O)
        self.winning_positions = [7, 56, 73, 84, 146, 273, 292, 448]

    def insert_x(self, position):
        if self.__is_valid_move(position - 1):
            self.X += int(math.pow(2, position - 1))

    def insert_o(self, position):
        if self.__is_valid_move(position - 1):
            self.O += int(math.pow(2, position - 1))

    def evaluate(self):

        if self.__evaluate_win_x():
            return 1

        if self.__evaluate_win_o():
            return -1

        if self.__evaluate_draw():
            return 0

        return 2

    def __evaluate_win_x(self):

        for winning_position in self.winning_positions:
            if (self.X & winning_position) == winning_position:
                return True

        return False

    def __evaluate_win_o(self):

        for winning_position in self.winning_positions:
            if (self.O & winning_position) == winning_position:
                return True

        return False

    def __evaluate_draw(self):

        if (self.X | self.O) == 511:
            return True

        return False

    def get_classic_board(self):
        board = "\n"

        for i in range(8, -1, -1):
            if i == 5 or i == 2:
                board = board + "\n" + "---------" + "\n"

            if (self.X & int(math.pow(2, i))) > 0:
                if i % 3 != 0:
                    board = board + "X | "
                else:
                    board = board + "X"
            elif (self.O & int(math.pow(2, i))) > 0:
                if i % 3 != 0:
                    board = board + "O | "
                else:
                    board = board + "O"
            else:
                if i % 3 != 0:
                    board = board + "  | "
                else:
                    board = board + " "

        return board + "\n"

    def get_binary_board(self, player):
        board = []
        row = []

        for i in range(8, -1, -1):
            cell = []

            if player == 'X':
                if (self.X & int(math.pow(2, i))) == 0:
                    cell.append(0)
                else:
                    cell.append(1)

                if (self.O & int(math.pow(2, i))) == 0:
                    cell.append(0)
                else:
                    cell.append(1)

            if player == 'O':
                if (self.O & int(math.pow(2, i))) == 0:
                    cell.append(0)
                else:
                    cell.append(1)

                if (self.X & int(math.pow(2, i))) == 0:
                    cell.append(0)
                else:
                    cell.append(1)

            row.append(cell)

            if i % 3 == 0:
                board.append(row)
                row = []

        return board

    def get_possible_moves(self):
        empty_positions = []
        for i in range(0, 9):
            if (self.X & int(math.pow(2, i))) == 0 and (self.O & int(math.pow(2, i))) == 0:
                empty_positions.append(i+1)

        return empty_positions

    def deep_copy(self):
        b = Board(self.X, self.O)
        return b

    def get_next_board_states(self, move):
        possible_moves = self.get_possible_moves()
        next_board_states = []

        for possible_move in possible_moves:
            b = self.deep_copy()
            if move == 'X':
                b.insert_x(possible_move)
            else:
                b.insert_o(possible_move)
            next_board_states.append(b)

        return next_board_states

    def __is_valid_move(self, position):
        if (self.X & int(math.pow(2, position))) == 0 and (self.O & int(math.pow(2, position))) == 0:
            return True
        return False


# b = Board()
# print(b.get_possible_moves())
# b.insert_x(5)
# print(b.get_possible_moves())
# print(b.get_classic_board())
# b.insert_o(9)
# print(b.get_possible_moves())
# print(b.get_classic_board())
# b.insert_x(1)
# print(b.get_possible_moves())
# print(b.get_classic_board())
# b.insert_o(7)
# print(b.get_classic_board())
# b.insert_x(8)
# print("evaluation: ", b.evaluate())
# print(b.get_classic_board())
# b.insert_o(2)
# print(b.get_classic_board())
# b.insert_x(6)
# print(b.get_classic_board())
# b.insert_o(4)
# print(b.get_classic_board())
# b.insert_x(3)
# print(b.get_classic_board())
# print("evaluation: ", b.evaluate())
#
# b1 = Board()
# b1.insert_o(3)
# b1.insert_o(5)
# b1.insert_o(7)
# print(b1.get_classic_board())
# print(b1.evaluate())



