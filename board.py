import math


class Board:

    def __init__(self):
        self.X = int(0)
        self.O = int(0)

    def insert_x(self, position):
        self.X += int(math.pow(2, position - 1))

    def insert_o(self, position):
        self.O += int(math.pow(2, position - 1))

    def evaluate(self):

        winning_positions = [7, 56, 73, 84, 146, 273, 292, 448]

        if self.__evaluate_win_x(winning_positions):
            return 1

        if self.__evaluate_win_o(winning_positions):
            return -1

        if self.__evaluate_draw():
            return 0

        return 2

    def __evaluate_win_x(self, winning_positions):

        for wp in winning_positions:
            if (self.X & wp) == wp:
                return True

        return False

    def __evaluate_win_o(self, winning_positions):

        for wp in winning_positions:
            if (self.O & wp) == wp:
                return True

        return False

    def __evaluate_draw(self):

        if (self.X | self.O) == 511:
            return True

        return False

    def get_classic_board(self):
        board = ""

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

        return board

    def get_binary_board(self):
        board = []
        board_x = []
        board_o = []
        row_x = []
        row_o = []

        for i in range(8, -1, -1):

            if (self.X & int(math.pow(2, i))) == 0:
                row_x.append(0)
            else:
                row_x.append(1)

            if (self.O & int(math.pow(2, i))) == 0:
                row_o.append(0)
            else:
                row_o.append(1)

            if i == 6 or i == 3 or i == 0:
                board_x.append(row_x)
                board_o.append(row_o)
                row_x = []
                row_o = []

        board.append(board_x)
        board.append(board_o)

        return board

    def get_possible_moves(self):
        empty_positions = []
        for i in range(0, 9):
            if (self.X & int(math.pow(2, i))) == 0 and (self.O & int(math.pow(2, i))) == 0:
                empty_positions.append(i+1)

        return empty_positions


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



