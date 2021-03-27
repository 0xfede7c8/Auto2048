import logging

import numpy as np
from numpy.random import randint, choice


logging.basicConfig(level=logging.DEBUG)


class Board:
    POSSIBLE_VALUES = np.array([2, 4])
    X = 1
    Y = 0

    def __init__(self, shape=(4, 4)):
        self.shape = shape
        self._initialize_board()

    def _initialize_board(self):
        self.state = np.zeros(self.shape, dtype=np.int32)
        # Initialize a random square with a random value
        x, y = self._get_random_square()
        value = self._get_random_value()
        logging.debug(f'Initializing square: X: {x} Y: {y} Value: {value}')
        self.state[x][y] = value

    def print(self):
        print(self.state)

    def _get_random_square(self):
        return randint(self.shape[Board.X]), randint(self.shape[Board.Y])

    def get_state(self):
        return self.state

    def get_current_score(self):
        return np.sum(self.state)

    @classmethod
    def _get_random_value(cls):
        '''
        :return: Returns 2 or 4, randomly
        '''
        return choice(cls.POSSIBLE_VALUES, p=[0.9, 0.1])    # .9 for 2 and .1 for 4

