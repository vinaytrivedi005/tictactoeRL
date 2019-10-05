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
    def get_move(self, board, turn):
        return


class RandomPlayer(Player):
    def get_move(self, board, turn):
        possible_moves = board.get_possible_moves()
        r = random.randint(0, len(possible_moves) - 1)
        return possible_moves[r]


class NNPlayer(Player):

    epochs = 0

    def __init__(self, name):
        self.name = name
        if os.path.isfile("./models/model.tf"):
            self.model = load_model("./models/model.tf",
                                    custom_objects=None,
                                    compile=True)
            self.alpha = 0.0
            self.epsilon = 0.0
        else:
            self.__create_model()
            self.alpha = 0.9
            self.epsilon = 0.9
        self.X_train = []
        self.O_train = []
        self.X_true = []
        self.O_true = []

    def set_epsilon(self, epsilon):
        self.epsilon = epsilon

    def __reset_data(self):
        self.X_train = []
        self.O_train = []
        self.X_true = []
        self.O_true = []

    def __create_model(self):
        self.model = Sequential()

        # Pre-processing data
        self.model.add(Lambda(lambda x: x / 1.0 - 0.5, input_shape=(3, 3, 2)))

        # Layer 1: convolution layer, input 65 x 320 x 3, output 63 x 318 x 32
        # model.add(Convolution2D(24, 5, 5, subsample=(2,2),activation="relu"))
        self.model.add(Convolution2D(10, 3, 3, activation="relu"))

        self.model.add(Flatten())

        self.model.add(Dense(5))
        self.model.add(Activation("relu"))
        self.model.add(Dropout(0.2))

        self.model.add(Dense(1))
        self.model.compile(loss='mse', optimizer='adam')

    def train(self, result):

        self.__fill_truth(result)
        length = len(self.X_train) + len(self.O_train)
        positions = np.asarray(self.X_train + self.O_train)
        positions = np.reshape(positions, (length, 3, 3, 2))
        truth = np.asarray(self.X_true + self.O_true)

        if NNPlayer.epochs % 100 == 0:
            self.alpha *= 0.9
            self.epsilon *= 0.9

        self.model.fit(positions, truth, validation_split=0.0, shuffle=True, epochs=1)

        save_model(self.model, './models/model.tf', overwrite=True, include_optimizer=True)
        self.__reset_data()
        NNPlayer.epochs += 1

    def __fill_truth(self, result):

        if result == 1:
            value = 1
            for i in range(len(self.X_train) - 1, -1, -1):
                self.X_true.append(value)
                value -= value*self.epsilon

            value = -1
            for i in range(len(self.O_train) - 1, -1, -1):
                self.O_true.append(value)
                value -= value*self.epsilon

        if result == -1:
            value = -1
            for i in range(len(self.X_train) - 1, -1, -1):
                self.X_true.append(value)
                value -= value * self.epsilon

            value = 1
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

    def get_move(self, board, turn):
        copy_board = []
        if turn == 0:
            copy_board = board.get_binary_board().copy()
            self.X_train.append(copy_board)
        else:
            copy_board.append(board.get_binary_board()[1].copy())
            copy_board.append(board.get_binary_board()[0].copy())
            self.O_train.append(copy_board)

        possible_moves = board.get_possible_moves()

        r = random.uniform(0, 1)

        if r < self.alpha:
            move_index = random.randint(0, len(possible_moves) - 1)
        else:
            board_states = self.__get_board_states(copy_board, possible_moves)
            maximum = float("-inf")
            move_index = 0
            for i in range(len(board_states)):
                prediction = self.predict(np.expand_dims(np.asarray(board_states[i]).T, axis=0))
                if maximum < prediction:
                    maximum = prediction
                    move_index = i

        return possible_moves[move_index]

    def __get_board_states(self, board, possible_moves):
        states = []

        for p in possible_moves:
            b = np.array(board, copy=True)
            if p == 1:
                row = 2
                col = 2
            if p == 2:
                row = 2
                col = 1
            if p == 3:
                row = 2
                col = 0
            if p == 4:
                row = 1
                col = 2
            if p == 5:
                row = 1
                col = 1
            if p == 6:
                row = 1
                col = 0
            if p == 7:
                row = 0
                col = 2
            if p == 8:
                row = 0
                col = 1
            if p == 9:
                row = 0
                col = 0
            b[0][row][col] = 1
            states.append(b)

        return states
