from game_logic import tic_tac_game
from graphics_board import graphics_board

"""file that runs the game"""


def run(size):
    game = tic_tac_game()
    game.play_game()


run(3)
