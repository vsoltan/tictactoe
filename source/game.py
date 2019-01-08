#!/usr/bin/env python

import random as r

import numpy as np
# version 1.1
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
        else:
            self.board = np.empty(shape=(boardSize, boardSize), dtype=str)

        if boardSize is None:
            self.size = 3
        else:
            self.size = boardSize

        # randomly selects the first player, player0 and player1
        self.curr_turn = r.choice([-1, 1])

        # token assignments: player1 -> O, player2 -> X
        self.token_dict = {-1: "O", 1: "X"}

        self.player_dict = {-1: "player1", 1: "player2"}

        # keeps track of the number of moves
        self.numTokens = 0

    """checks whether the game is complete, win or draw"""

    def game_over(self, playerToken):
        """not possible to lose without taking at least 5 turns (3 x 3), 7 (4 x 4) etc"""

        if self.numTokens < 2 * self.size - 1:
            return False

        """check the columns"""

        """
        smallest probe [[X, X, X]...] -> one space between each x
        largest probe [[X, O, O], 
                       [O, X, O],  
                       [O, O, X]] -> 4 (size + 1) spaces between each x 
        """
        return False

    """game logic, alternating players choosing a space on the board to fill with their respective token"""

    def play_game(self, player):
        token = self.token_dict[self.curr_turn]

        while self.game_over(token) != True:
            # user choice
            # NEED TO ADD user input error handling (not adding to an already full space)
            move_row, move_col = map(int, raw_input(
                self.player_dict[self.curr_turn] + " make your move: input row and column").split())

            # updating the visual and computational representations of the board
            self.board[move_row][move_col] = token
            self.list_board[(move_row + 1) * (move_col + 1) - 1] = token

            # alternate users
            self.curr_turn = -1 * self.curr_turn

            # increase the number of tokens
            self.numTokens += 1

            # repaint board
            self.print_board()

            self.print_list_board()

    """different board manipulations"""

    def print_board(self):
        print(self.board)

    def check_Columns(self, token): #doesn't work
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.board[i][j] != token:
                    return False
        return True

    def check_Rows(self):
        return 0;


game = tic_tac_Game(None)
game.print_board()
game.play_game(game.curr_turn)
