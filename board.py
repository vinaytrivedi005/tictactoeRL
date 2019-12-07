import math


class Board:

    def __init__(self, X, O):
        self.X = int(X)
        self.O = int(O)
        self.winning_positions = [7, 56, 73, 84, 146, 273, 292, 448]

    def insert_x(self, position):
        if self.is_valid_move(position - 1):
            self.X += int(math.pow(2, position - 1))

    def insert_o(self, position):
        if self.is_valid_move(position - 1):
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

        if self.evaluate() == 2:
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

    def is_valid_move(self, position):
        if (self.X & int(math.pow(2, position))) == 0 and (self.O & int(math.pow(2, position))) == 0:
            return True
        return False


class UBoard:
    """
    Board of this game looks like below:

     81| 80| 79| 78| 77| 76| 75| 74| 73
    ---|---|---|---|---|---|---|---|---
     72| 71| 70| 69| 68| 67| 66| 65| 64
    ---|---|---|---|---|---|---|---|---
     63| 62| 61| 60| 59| 58| 57| 56| 55
    ---|---|---|---|---|---|---|---|---
     54| 53| 52| 51| 50| 49| 48| 47| 46
    ---|---|---|---|---|---|---|---|---
     45| 44| 43| 42| 41| 40| 39| 38| 37
    ---|---|---|---|---|---|---|---|---
     36| 35| 34| 33| 32| 31| 30| 29| 28
    ---|---|---|---|---|---|---|---|---
     27| 26| 25| 24| 23| 22| 21| 20| 19
    ---|---|---|---|---|---|---|---|---
     18| 17| 16| 15| 14| 13| 12| 11| 10
    ---|---|---|---|---|---|---|---|---
     9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1

     81| 80| 79| 78| 77| 76|
    ---|---|---|---|---|---|
     72| 71| 70| 69| 68| 67|    8
    ---|---|---|---|---|---|
     63| 62| 61|           |
    ---|---|---|---|---|---|---|---|---
               |           |
               |           |
         6     |     5     |    4
               |           |
               |           |
    ---|---|---|---|---|---|---|---|---
               |           |
               |           |
         3     |     2     |    1
               |           |
               |           |


    """

    def __init__(self, moves):
        self.moves = moves
        self.super_board = Board(0, 0)
        self.sub_boards = self.__create_sub_boards()
        self.__reach_position(moves)

    @staticmethod
    def __create_sub_boards():
        boards = {}
        for i in range(9):
            b = Board(0, 0)
            boards[i] = b

        return boards

    def __reach_position(self, moves):
        for i in range(len(moves)):
            if i % 2 == 0:
                self.insert_x(moves[i])
            else:
                self.insert_o(moves[i])

    def insert_x(self, position):
        board, board_id, move = self.__get_board(position - 1)

        if not self.is_valid_move(board, move):
            return

        board.insert_x(move)
        self.moves.append(position - 1)
        if board.evaluate() == 1:
            self.super_board.insert_x(board_id + 1)

    def insert_o(self, position):
        board, board_id, move = self.__get_board(position - 1)

        if not self.is_valid_move(board, move):
            return

        board.insert_o(move)
        self.moves.append(position - 1)
        if board.evaluate() == -1:
            self.super_board.insert_o(board_id + 1)

    def __get_board(self, position):
        board_col = position % 9
        board_row = position % 27
        board_id = UBoard.__ternary_to_decimal(str(board_row) + str(board_col))
        position_col = position % 3
        position_row = (position % 9) % 3
        position = UBoard.__ternary_to_decimal(str(position_row) + str(position_col))
        board = self.sub_boards[board_id]
        return board, board_id, position

    @staticmethod
    def __ternary_to_decimal(ternary_num):
        power = 0
        decimal_num = 0
        for i in range(len(ternary_num)-1, -1, -1):
            decimal_num += int(ternary_num[i]) * math.pow(3, power)
            power += 1
        return decimal_num

    def evaluate(self):
        if self.super_board.evaluate() != 2:
            return self.super_board.evaluate()
        elif len(self.get_possible_moves()) == 0:
            return 0
        else:
            return 2

    def get_possible_moves(self):
        empty_positions = []

        if self.super_board.evaluate() == 2:
            last_move = self.moves[-1]
            board_id = last_move % 9
            board_to_move = self.sub_boards[board_id]
            if board_to_move.evaluate() == 2:
                empty_positions = [board_id*9 + move for move in board_to_move.get_possible_moves()]
            else:
                for board_id in self.sub_boards.keys():
                    empty_positions = [board_id*9 + move for move in self.sub_boards[board_id].get_possible_moves()]

        return empty_positions

    def deep_copy(self):
        b = UBoard(self.moves)
        return b

    def get_binary_board(self, player):
        board = []
        row = []

        for position in range(80, -1, -1):
            cell = []

            if player == 'X':
                board, board_id, move = self.__get_board(position)
                if (board.X & int(math.pow(2, move))) == 0:
                    cell.append(0)
                else:
                    cell.append(1)

                if (board.O & int(math.pow(2, move))) == 0:
                    cell.append(0)
                else:
                    cell.append(1)

            if player == 'O':
                board, board_id, move = self.__get_board(position)

                if (board.O & int(math.pow(2, move))) == 0:
                    cell.append(0)
                else:
                    cell.append(1)

                if (board.X & int(math.pow(2, move))) == 0:
                    cell.append(0)
                else:
                    cell.append(1)

            row.append(cell)

            if position % 9 == 0:
                board.append(row)
                row = []

        return board

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

    def is_valid_move(self, board, move):
        return board.is_valid_move(move)


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



