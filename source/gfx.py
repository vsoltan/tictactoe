from graphics import *

from game import tic_tac_Game


def main():
    # before

    win = GraphWin("Tic Tac Toe", 500, 500)
    win.setBackground(color_rgb(0, 0, 0))
    game = tic_tac_Game(3)

    print(GraphWin.getHeight(win))

    #creating the board
    for i in range(1, game.size):

        horiz_grid = i * win.getWidth() / game.size
        vert_grid = i * win.getHeight() / game.size

        horizontal_bound = Line(Point(horiz_grid, 0), Point(horiz_grid, win.getHeight()))
        vertical_bound = Line(Point(0, vert_grid), Point(win.getWidth(), vert_grid))
        horizontal_bound.setFill("white")
        vertical_bound.setFill("white")
        horizontal_bound.draw(win)
        vertical_bound.draw(win)

    




    # message = Text(Point(250, 250), "Hello!")
    # message.setTextColor("white")
    # message.draw(win)

    ## can add some transition

    win.getMouse()  # Pause to view result
    win.close()  # Close window when done


main()
