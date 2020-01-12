import abc
import random
import os
import numpy as np
from tensorflow.keras.models import Sequential, load_model, save_model
from tensorflow.keras.layers import Flatten, Dense, Lambda, Activation, Dropout, Convolution2D


class Player:
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def get_move(self, game):
        return


class RandomPlayer(Player):
    def get_move(self, game):
        possible_moves = game.get_board().get_possible_moves()
        r = random.randint(0, len(possible_moves) - 1)
        return possible_moves[r]


class NNPlayer(Player):

    epochs = 0

    def __init__(self, name, game_name, model_path):
        self.name = name
        self.game_name = game_name
        self.model_path = model_path
        if os.path.isfile(model_path):
            self.model = load_model(model_path,
                                    custom_objects=None,
                                    compile=True)
            self.alpha = 0.9
            self.epsilon = 0.1
        else:
            NNPlayer.epochs = 0
            self.__create_model()
            self.alpha = 0.9
            self.epsilon = 0.1
        self.X_train = []
        self.O_train = []
        self.X_true = []
        self.O_true = []
        self.is_training = False

    def set_is_training(self, is_training):
        self.is_training = is_training

    def set_epsilon(self, epsilon):
        self.epsilon = epsilon

    def __reset_data(self):
        self.X_train = []
        self.O_train = []
        self.X_true = []
        self.O_true = []

    def __create_model(self):
        if self.game_name == 'TTT':
            self.model = Sequential()

            # Pre-processing data
            self.model.add(Lambda(lambda x: x / 1.0 - 0.5, input_shape=(3, 3, 2)))

            # Layer 1: convolution layer, input 65 x 320 x 3, output 63 x 318 x 32
            # model.add(Convolution2D(24, 5, 5, subsample=(2,2),activation="relu"))
            self.model.add(Convolution2D(9, (3, 3), activation="relu"))

            self.model.add(Flatten())

            self.model.add(Dense(3))
            self.model.add(Activation("relu"))
            self.model.add(Dropout(0.2))

            self.model.add(Dense(1))
            self.model.compile(loss='mse', optimizer='adam')

        if self.game_name == 'UTTT':
            self.model = Sequential()

            # Pre-processing data
            self.model.add(Lambda(lambda x: x / 1.0 - 0.5, input_shape=(9, 9, 2)))

            # Layer 1: convolution layer, input 9 x 9 x 2, output 7 x 7 x 9
            self.model.add(Convolution2D(9, (3, 3), activation="relu", strides=(1, 1), padding='valid'))

            # Layer 1: convolution layer, input 7 x 7 x 9, output 5 x 5 x 27
            self.model.add(Convolution2D(27, (3, 3), activation="relu", strides=(1, 1), padding='valid'))

            # Layer 1: convolution layer, input 5 x 5 x 27, output 3 x 3 x 81
            self.model.add(Convolution2D(81, (3, 3), activation="relu", strides=(1, 1), padding='valid'))

            self.model.add(Flatten())

            self.model.add(Dense(100))
            self.model.add(Activation("relu"))
            self.model.add(Dropout(0.2))

            self.model.add(Dense(10))
            self.model.add(Activation("relu"))
            self.model.add(Dropout(0.2))

            self.model.add(Dense(1))
            self.model.compile(loss='mse', optimizer='adam')

    def train(self, result):

        self.__fill_truth(result)
        X = np.asarray(self.X_train + self.O_train)
        y = np.asarray(self.X_true + self.O_true)

        if NNPlayer.epochs % 100 == 0:
            self.alpha *= 0.8

        self.model.fit(X, y, validation_split=0.0, shuffle=True, epochs=1)

        save_model(self.model, self.model_path, overwrite=True, include_optimizer=True)
        self.__reset_data()
        NNPlayer.epochs += 1

    def __fill_truth(self, result):

        if result == 1:
            value = 10
            for i in range(len(self.X_train) - 1, -1, -1):
                self.X_true.append(value)
                value -= value*self.epsilon

            value = -10
            for i in range(len(self.O_train) - 1, -1, -1):
                self.O_true.append(value)
                value -= value*self.epsilon

        if result == -1:
            value = -10
            for i in range(len(self.X_train) - 1, -1, -1):
                self.X_true.append(value)
                value -= value * self.epsilon

            value = 10
            for i in range(len(self.O_train) - 1, -1, -1):
                self.O_true.append(value)
                value -= value * self.epsilon

        if result == 0:
            for x in self.X_train:
                self.X_true.append(0)

            for o in self.O_train:
                self.O_true.append(0)

    def predict(self, X):
        return self.model.predict(X)

    def get_move(self, game):
        if self.is_training:
            if game.turn == 'X':
                self.X_train.append(game.get_board().get_binary_board(game.turn))
            else:
                self.O_train.append(game.get_board().get_binary_board(game.turn))

        possible_moves = game.get_board().get_possible_moves()

        r = random.uniform(0, 1)

        if self.is_training and r < self.alpha:
            move_index = random.randint(0, len(possible_moves) - 1)
        else:
            score, move_index = self.__minimax(0, [game.get_board()], 0, True, 1, game, game.turn, game.turn)

        return possible_moves[move_index]

    def __minimax(self, cur_depth, boards, board_index, max_turn, target_depth, game, move, init_move):

        if boards[board_index].evaluate() != 2:
            if self.is_training:
                if move == 'X':
                    self.X_train.append(boards[board_index].get_binary_board(move))
                else:
                    self.O_train.append(boards[board_index].get_binary_board(move))
            if init_move == 'X':
                return boards[board_index].evaluate() * 10, board_index
            else:
                return boards[board_index].evaluate() * (-10), board_index

        if cur_depth == target_depth:
            if self.is_training:
                if move == 'X':
                    self.X_train.append(boards[board_index].get_binary_board(move))
                else:
                    self.O_train.append(boards[board_index].get_binary_board(move))
            score = self.predict(np.expand_dims(np.asarray(boards[board_index].get_binary_board(move)), axis=0))
            return score, board_index

        if max_turn:
            next_board_states = game.get_board().get_next_board_states(move)
            scores = []
            indexes = []

            if move == 'X':
                move = 'O'
            else:
                move = 'X'

            for i in range(len(next_board_states)):
                score, index = self.__minimax(cur_depth + 1,
                                              next_board_states,
                                              i,
                                              False,
                                              target_depth,
                                              game,
                                              move,
                                              init_move)
                scores.append(score)
                indexes.append(index)

            maximum = float("-inf")
            max_index = 0
            for i in range(len(scores)):
                if maximum < scores[i]:
                    maximum = scores[i]
                    max_index = indexes[i]
            return maximum, max_index
        else:
            next_board_states = game.get_board().get_next_board_states(move)
            scores = []
            indexes = []

            if move == 'X':
                move = 'O'
            else:
                move = 'X'

            for i in range(len(next_board_states)):
                score, index = self.__minimax(cur_depth + 1,
                                              next_board_states,
                                              i,
                                              True,
                                              target_depth,
                                              game,
                                              move,
                                              init_move)
                scores.append(score)
                indexes.append(index)

            minimum = float("inf")
            min_index = 0
            for i in range(len(scores)):
                if minimum > scores[i]:
                    minimum = scores[i]
                    min_index = indexes[i]
            return minimum, min_index
