from graphics import *


# from game_logic import tic_tac_game

class graphics_board:

    def __init__(self, boardSize):
        """

        :rtype: object

        initializes the board based on the parameters passed from the game obj

        """

        self.win = GraphWin("Tic Tac Toe", 500, 500)
        self.size = self.win.getHeight()
        self.win.setBackground(color_rgb(0, 0, 0))

        self.limits = [self.size / boardSize]

        for i in range(1, boardSize):
            horiz_grid = i * self.size / boardSize

            self.limits.append((i + 1) * self.limits[0])

            """increments for each block
            
            iteratively generates the board, draws the divisions an 
                equal distance from one another 

                            _|_|_
                            _|_|_  
                             | |   
            """

            horizontal_bound = Line(Point(horiz_grid, 0), Point(horiz_grid, self.size))
            vertical_bound = Line(Point(0, horiz_grid), Point(self.size, horiz_grid))

            horizontal_bound.setFill("white")
            vertical_bound.setFill("white")

            horizontal_bound.draw(self.win)
            vertical_bound.draw(self.win)

    def from_point_to_index(self, collection, coordinate):

        if coordinate >= collection[len(collection) - 1]:
            return -1

        i = 0

        while i < len(collection) and coordinate > collection[i]:
            print(coordinate)
            print(collection[0])
            i += 1
        return i


if __name__ == "__main__":
    game = graphics_board(3)
    print(game.from_point_to_index(game.limits, 500))
