from game_logic import tic_tac_game

"""file that runs the game"""


def run(size):
    game = tic_tac_game(size)
    game.play_game()


run(3)
