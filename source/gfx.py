from graphics import *
from game import tic_tac_Game


def main():
    win = GraphWin("Tic Tac Toe", 500, 500)
    win.setBackground(color_rgb(0, 0, 0))

    message = Text(Point(250, 250), "Hello!")
    message.setTextColor("white")
    message.draw(win)

    ## can add some transition

    win.getMouse()  # Pause to view result
    win.close()  # Close window when done


main()
