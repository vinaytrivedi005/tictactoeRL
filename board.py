import math
from ttt_exceptions import InvalidMoveException


class Board:

    def __init__(self, X, O):
        self.X = int(X)
        self.O = int(O)
        self.winning_positions = [7, 56, 73, 84, 146, 273, 292, 448]

    def insert_x(self, position):
        if self.is_valid_move(position - 1):
            self.X += int(math.pow(2, position - 1))
        else:
            raise InvalidMoveException("Invalid move: " + str(position))

    def insert_o(self, position):
        if self.is_valid_move(position - 1):
            self.O += int(math.pow(2, position - 1))
        else:
            raise InvalidMoveException("Invalid move: " + str(position))

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

     8 | 8 | 7 | 78| 77| 76|
    ---|---|---|---|---|---|
     6 | 5 | 4 | 69| 68| 67|    7
    ---|---|---|---|---|---|
     3 | 2 | 1 |           |
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
        """
        creates 9 sub boards of 3x3 using Board class.

        :return: dictionary of sub boards mapped with id 0-8
        """
        boards = {}
        for i in range(9):
            b = Board(0, 0)
            boards[i] = b

        return boards

    def __reach_position(self, moves):
        """
        makes the initials moves to reached the position in case UBoard is initialized with non empty moves.

        :param moves: list of moves already made before initializing board.
        :return: None
        """
        for i in range(len(moves)):
            if i % 2 == 0:
                self.insert_x(moves[i])
            else:
                self.insert_o(moves[i])

    def insert_x(self, position):
        """
        inserts move at specified position. position is between 1-81

        :param position: integer value between 1-81
        :return: None
        """

        # check if move is valid
        if not self.__is_valid_move(position):
            raise InvalidMoveException("Invalid move: " + str(position))

        # get sub board and the move on that sub board from position. move will be between 0-8
        board, board_id, move = self.__get_board(position - 1)

        board.insert_x(move + 1)   # making the move on the sub board. Board expects move to be between 1-9.

        self.moves.append(position)

        # if sub board is won with the move then make entry in the position of super board.
        if board.evaluate() == 1:
            self.super_board.insert_x(board_id + 1)   # Board expects move to be between 1-9 and board_id is between 0-8

    def insert_o(self, position):
        """
        inserts move at specified position. position is between 1-81

        :param position: integer value between 1-81
        :return: None
        """

        # check if move is valid
        if not self.__is_valid_move(position):
            raise InvalidMoveException("Invalid move: " + str(position))

        # get sub board and the move on that sub board from position. move will be between 0-8
        board, board_id, move = self.__get_board(position - 1)

        board.insert_o(move + 1)   # making the move on the sub board. Board expects move to be between 1-9.

        self.moves.append(position)

        # if sub board is won with the move then make entry in the position of super board.
        if board.evaluate() == -1:
            self.super_board.insert_o(board_id + 1)   # Board expects move to be between 1-9 and board_id is between 0-8

    def __get_board(self, position):
        """
        returns board, board_id and move from the position.

        :param position: integer value between 0-80
        :return: board object, board_id[0-8] and move[0-8]
        """
        board_id = UBoard.__get_super_board_square(position)  # get sub board id from position
        position = UBoard. __get_sub_board_square(position)   # get sub board square from position
        board = self.sub_boards[board_id]
        return board, board_id, position

    @staticmethod
    def __get_super_board_square(position):
        """
        returns sub board id from position.

        :param position: int between 0-80
        :return: sub board id[0-8] on which move has to be made.
        """

        # column of the sub board between 0-2
        board_col = (position % 9) // 3

        # row of the sub board between 0-2
        board_row = (position // 9) // 3

        return UBoard.__ternary_to_decimal(str(board_row) + str(board_col))

    @staticmethod
    def __get_sub_board_square(position):
        """
        returns square of sub board on which move has to be made.

        :param position: int value between 0-80
        :return: square on which move has to be made on sub board between 0-8.
        """

        # column of the sub board square between 0-2
        position_col = position % 3

        # row of the sub board square between 0-2
        position_row = (position // 9) % 3

        return UBoard.__ternary_to_decimal(str(position_row) + str(position_col))

    @staticmethod
    def __ternary_to_decimal(ternary_num):
        """
        converts turnary number to decimal.

        :param ternary_num: string containing turnary number value with digits between 0-2
        :return: int with corresponding decimal value.
        """

        power = 0
        decimal_num = 0

        for i in range(len(ternary_num)-1, -1, -1):
            decimal_num += int(ternary_num[i]) * math.pow(3, power)
            power += 1
        return int(decimal_num)

    def evaluate(self):
        """
        evaluating the current board position.

        :return: 1 if X wins, -1 if O wins, 0 if draw and 2 if game still undecided.
        """

        # if super board is decisive
        if self.super_board.evaluate() != 2:
            return self.super_board.evaluate()

        # if no possible moves to make
        if len(self.get_possible_moves()) == 0:
            return 0

        return 2

    def get_possible_moves(self):
        """
        returns the list of possible moves.

        :return: list of integers between 1-81 which are possible moves on the board given current state.
        """
        empty_positions = []

        # if super board is not decisive
        if self.super_board.evaluate() == 2:
            free_move = False

            # if it is first move of the game then player can make move on any available square.
            if len(self.moves) == 0:
                print("--------- moves length =0")
                free_move = True

            # if it is not first move then player has to make move on the board corresponding to the square of previous
            # move.
            else:
                last_move = self.moves[-1]  # get the last move of the game.

                # sub board square on which last move is made will be the board id on which next move has to be made.
                board_id = UBoard.__get_sub_board_square(last_move - 1)
                board_to_move = self.sub_boards[board_id]

                # if board to move is not decisive then return possible moves on that board.
                if board_to_move.evaluate() == 2:
                    for move in board_to_move.get_possible_moves():
                        position = UBoard.__get_uboard_square(board_id, move)
                        empty_positions.append(position)

                # if board to move is already decided then return all possible moves on entire 9x9 board.
                else:
                    free_move = True

            # if the move is not restricted in any specific sub board
            if free_move:
                print(self.sub_boards.keys())
                for board_id in self.sub_boards.keys():
                    print(self.sub_boards[board_id].evaluate(), board_id, self.sub_boards[board_id].get_possible_moves())
                    # if board is not yet decided then add all possible moves on that board.
                    if self.sub_boards[board_id].evaluate() == 2:
                        for move in self.sub_boards[board_id].get_possible_moves():
                            position = UBoard.__get_uboard_square(board_id, move)
                            empty_positions.append(position)

        return empty_positions

    @staticmethod
    def __get_uboard_square(sub_board_id, sub_board_square):
        """
        returns uboard square between 1-81 from sub board id and sub board square
        :param sub_board_id: id of the sub board between 0-8
        :param sub_board_square: square of the sub board between 0-8
        :return: position between 1-81

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

         9 | 8 | 7 | 78| 77| 76|
        ---|---|---|---|---|---|
         6 | 5 | 4 | 69| 68| 67|    7
        ---|---|---|---|---|---|
         3 | 2 | 1 |           |
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

        board_division = sub_board_id // 3
        board_position_div = board_division * 27

        board_reminder = sub_board_id % 3
        board_position_rem = board_reminder * 3

        move_division = sub_board_square // 3
        move_position_div = move_division * 9

        move_reminder = sub_board_square % 3

        position = board_position_div + board_position_rem + move_position_div + move_reminder

        return position + 1

    def deep_copy(self):
        """
        deep copy the current UBoard object.

        :return: replica of UBoard object.
        """
        b = UBoard(self.moves)
        return b

    def get_binary_board(self, player):
        """
        return 9x9x2 binary board from the reference of specified player.

        :param player: player on whose reference binary board has to be created.
        :return: 9x9x2 binary board
        """
        b = []
        row = []

        for position in range(80, -1, -1):
            cell = []

            if player == 'X':
                board, board_id, move = self.__get_board(position)

                # if board doesn't have x on the specified move position
                if (board.X & int(math.pow(2, move))) == 0:
                    cell.append(0)

                # if board does have x on the specified move position
                else:
                    cell.append(1)

                # if board doesn't have o on the specified move position
                if (board.O & int(math.pow(2, move))) == 0:
                    cell.append(0)

                # if board does have o on the specified move position
                else:
                    cell.append(1)

            if player == 'O':
                board, board_id, move = self.__get_board(position)

                # if board doesn't have o on the specified move position
                if (board.O & int(math.pow(2, move))) == 0:
                    cell.append(0)

                # if board does have o on the specified move position
                else:
                    cell.append(1)

                # if board doesn't have x on the specified move position
                if (board.X & int(math.pow(2, move))) == 0:
                    cell.append(0)

                # if board does have x on the specified move position
                else:
                    cell.append(1)

            row.append(cell)

            if position % 9 == 0:
                b.append(row)
                row = []

        return b

    def get_next_board_states(self, player):
        """
        returns all possible next board states for the specified player.

        :param player: player for with next board states are requested.
        :return: array of board states
        """

        possible_moves = self.get_possible_moves()
        next_board_states = []

        for possible_move in possible_moves:
            b = self.deep_copy()
            if player == 'X':
                b.insert_x(possible_move)
            else:
                b.insert_o(possible_move)
            next_board_states.append(b)

        return next_board_states

    def __is_valid_move(self, position):
        """
        validates the move on the specified board.

        :param position: move to be validated
        :return: True if move is valid, False otherwise
        """
        print(self.get_possible_moves(), position)
        if position in self.get_possible_moves():
            return True
        else:
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



