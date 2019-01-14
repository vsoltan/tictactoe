#!/usr/bin/env python

import random as r

import numpy as np

from graphics_board import graphics_board

# version 1.4
# author vsoltan

""""framework for a basic tic tac toe game"""


class tic_tac_game:

    def __init__(self, boardSize=3):
        """
        :rtype: object
        :arg: size of the desired board, number
              of tokens in a row required for a win

        creates a board with passed specifications, default 3 x 3
        assigns player order and their associated tokens

        """
        self.size = boardSize

        self.board = np.empty(shape=(self.size, self.size), dtype=str)

        self.visual_board = graphics_board(self.size)

        # randomly selects the first player, player0 and player1
        self.curr_turn = r.choice([-1, 1])

        # token assignments: player1 -> X, player2 -> O
        self.token_dict = {-1: "X", 1: "O"}

        self.image_dict = {-1: "placeholder1.gif", 1: "placeholder1.gif"}

        self.player_dict = {-1: "player1", 1: "player2"}

        self.score = {-1: 0, 1: 0}

        self.num_turns = 0

    def game_over(self):
        """checks whether the game is complete, win or draw"""

        # not possible to lose without taking at least 5 turns (3 x 3), 7 (4 x 4) etc
        if self.num_turns < 2 * self.size - 1:
            return False

        if self.check_columns() is True:  # can maybe write in a more pythonian way?
            return True

        if self.check_rows() is True:
            return True


        if self.check_diagonals() is True:
            return True

        return False

    def play_game(self):
        """game logic, alternating players choosing spaces on the board to fill with their respective tokens"""

        is_over = False

        while not is_over and self.num_turns != self.size ** 2:
            token = self.token_dict[self.curr_turn]

            # user input validation: can't select the same space twice
            while True:

                print("Make your move!")
                click_point = self.visual_board.win.getMouse()
                lims = self.visual_board.limits

                move_col = self.visual_board.from_point_to_index(lims, click_point.getX())

                move_row = self.visual_board.from_point_to_index(lims, click_point.getY())

                # move_row, move_col = map(int, input(self.player_dict[self.curr_turn] +
                #                                     " make your move: input row and column").split())

                if self.board[move_row][move_col] == '':
                    break
                else:
                    print("index is full, choose another space")

            # updating the visual representation of the board
            self.board[move_row][move_col] = token

            # increase the number of tokens
            self.num_turns += 1

            is_over = self.game_over()

            # alternate users
            self.curr_turn = -1 * self.curr_turn

            # repaint board
            self.print_board()

        if self.num_turns == self.size ** 2 and not is_over:  ## if board is full but game is not over -> draw
            print("game is a draw!")
        else:
            print(self.player_dict[-1 * self.curr_turn] + " wins!")
            self.score[-1 * self.curr_turn] += 1

        # play again?
        cont = input("play again (y/n)?")

        # temp user validation (could be another character)
        if cont == 'y':
            is_over = False
            self.board = np.empty(shape=(self.size, self.size), dtype=str)
            # player that just lost gets first turn
            self.play_game()
        else:
            return

    # board functions
    def print_board(self):
        print(self.board)

    def check_rows(self):
            for i in range(0, self.size):
                consecutive_tokens = 0
                for j in range(0, self.size):
                    if self.board[i][j] == self.token_dict[self.curr_turn]:
                        consecutive_tokens += 1
                if consecutive_tokens == self.size:
                    return True
            return False

    def check_columns(self):
            for i in range(0, self.size):
                consecutive_tokens = 0
                for j in range(0, self.size):
                    if self.board[j][i] == self.token_dict[self.curr_turn]:
                        consecutive_tokens += 1
                if consecutive_tokens == self.size:
                    return True
            return False

    def check_diagonals(self):
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


if __name__ == "__main__":
    game = tic_tac_game()

