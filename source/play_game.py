from game_logic import tic_tac_game
from graphics_board import graphics_board

"""file that runs the game"""


def run(size):
    visual = graphics_board(3, tic_tac_game())


# run(3)
