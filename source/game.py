#!/usr/bin/env python

import random as r

import numpy as np
# version 1.0
# author vsoltan
from pip._vendor.distlib.compat import raw_input

""""framework for a basic tic tac toe game"""


class tic_tac_Game:

    def __init__(self, boardSize):
        """
        :rtype: object
        :arg: size of the desired board, also the number
                of tokens in a row required for a win

        creates a board with passed specifications, default 3 x 3
        assigns player order and their associated tokens

        """
        if boardSize is None:
            self.board = np.empty(shape=(3, 3), dtype=str)
            self.list_board = np.empty(9, dtype=str)
        else:
            self.board = np.empty(shape=(boardSize, boardSize), dtype=str)
            self.list_board = np.empty(boardSize ** 2, dtype=str)

        self.size = boardSize

        """randomly selects the first player, player0 and player1"""
        self.curr_turn = r.choice([-1, 1])

        """token assignments: player1 -> O, player2 -> X"""
        self.token_dict = {-1: "O", 1: "X"}

        self.player_dict = {-1: "player1", 1: "player2"}

        """keeps track of the number of moves, used in the win condition(game_over) method"""
        self.numTokens = 0

    """checks whether the game is complete, win or draw"""

    def game_over(self, player, size):
        """not possible to lose without taking at least 5 turns (3 x 3), 7 (4 x 4) etc"""
        if self.numTokens < 2 * self.size - 1:
            return True

        """probing to find connected tokens"""

        # """
        #
        #
        # """
        # for i in range(1, self.size + 2):

        return False

    """game logic, alternating players choosing a space on the board to fill with their respective token"""

    def play_game(self, player):
        while self.game_over() != True:
            moveRow, moveCol = map(int, raw_input(
                self.player_dict[self.curr_turn] + " make your move: input row and column").split())
            self.board[moveRow][moveCol] = self.token_dict[self.curr_turn]
            self.curr_turn = -1 * self.curr_turn
            self.numTokens += 1
            self.print_board()

    """prints out the board, used for debugging purposes"""

    def print_board(self):
        print(self.board)

    def print_list_board(self):
        print(self.list_board)


game = tic_tac_Game(None)
# game.print_board()
# game.play_game(game.curr_turn)
game.print_list_board()
