#!/usr/bin/env python

import random as r

import numpy as np
import pip._vendor.distlib.compat #cleanup this import?

# version 1.2
# author vsoltan

""""framework for a basic tic tac toe game"""


class tic_tac_Game:

    def __init__(self, boardSize):
        """
        :rtype: object
        :arg: size of the desired board, number
              of tokens in a row required for a win

        creates a board with passed specifications, default 3 x 3
        assigns player order and their associated tokens

        """
        if boardSize is None:
            self.size = 3
        else:
            self.size = boardSize

        self.board = np.empty(shape=(self.size, self.size), dtype=str)

        # randomly selects the first player, player0 and player1
        self.curr_turn = r.choice([-1, 1])

        # token assignments: player1 -> X, player2 -> O
        self.token_dict = {-1: "X", 1: "O"}

        self.player_dict = {-1: "player1", 1: "player2"}

        self.num_turns = 0

    """checks whether the game is complete, win or draw"""

    def game_over(self, playerToken):

        # not possible to lose without taking at least 5 turns (3 x 3), 7 (4 x 4) etc
        if self.num_turns < 2 * self.size - 1:
            return False

        if self.check_columns(self.board, playerToken) is True: # can maybe write in a more pythonian way?
            return True

        temp_board = np.transpose(self.board)

        if self.check_columns(temp_board, playerToken) is True:
            return True

        if self.check_diagonals(playerToken) is True:
            return True

        return False

    """game logic, alternating players choosing a space on the board to fill with their respective token"""

    def play_game(self, player):

        is_over = False

        while not is_over and self.num_turns != self.size ** 2:
            token = self.token_dict[self.curr_turn]

            # user choice
            # NEED TO ADD user input error handling (not adding to an already full space)
            move_row, move_col = map(int, pip._vendor.distlib.compat.raw_input(
                self.player_dict[self.curr_turn] + " make your move: input row and column").split())

            # updating the visual representation of the board
            self.board[move_row][move_col] = token

            # increase the number of tokens
            self.num_turns += 1

            is_over = self.game_over(token)

            # alternate users
            self.curr_turn = -1 * self.curr_turn

            # repaint board
            self.print_board()

        if self.num_turns == self.size ** 2 and not is_over:  ## if board is full but game is not over -> draw
            print("game is a draw!")
        else:
            print(self.player_dict[-1 * self.curr_turn] + " wins!")

    """board functions"""

    def print_board(self):
        print(self.board)

    def check_columns(self, board, token):
        for i in range(0, self.size):
            consecutive_tokens = 0
            for j in range(0, self.size):
                if board[i][j] == token:
                    consecutive_tokens += 1
            if consecutive_tokens == self.size:
                return True
        return False

    def check_diagonals(self, token):
        diag = np.diag(self.board)
        other_diag = np.diag(np.fliplr(self.board))

        consecutive_tokens = 1
        """initialized to 1 due to comparison-based iteration 
                ex: a = b = c -> comparing a, b, c -> (a,b) and (b,c)
                    2 comparisons for 3 consecutive tokens"""

        for i in range(0, len(diag) - 1):
            if diag[i] == diag[i + 1]:
                consecutive_tokens += 1
            if consecutive_tokens == self.size:
                return True
        else:
            consecutive_tokens = 1
        for i in range(0, len(other_diag) - 1):
            if other_diag[i] == other_diag[i + 1]:
                consecutive_tokens += 1
            if consecutive_tokens == self.size:
                return True
        return False


game = tic_tac_Game(3)
game.print_board()
game.play_game(game.curr_turn)
# game.board = [['X', 'X', 'O'], ['O', 'O', 'X'], ['O', '', '']]
# print(game.check_diagonals('O'))
