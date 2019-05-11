from graphics import *


class graphics_board:

    def __init__(self, board_size):
        """
        :rtype: object

        initializes the board based on the parameters passed from the game obj

        """

        self.win = GraphWin("Tic Tac Toe", 500, 500)
        self.size = self.win.getHeight()
        self.win.setBackground(color_rgb(0, 0, 0))
        self.board_size = board_size
        self.tokens_drawn = []
        self.structs = []
        self.limits = [self.size / self.board_size]
        self.game_mode = 0

    """choose between two game modes that leverage different logic"""

    def draw_menu_single_or_multiplayer(self):

        # welcoming screen
        welcome = Text(Point(250, 62.5), "Tic Tac Toe")
        welcome.setSize(32)
        welcome.setFill('white')
        self.structs.append(welcome)
        welcome.draw(self.win)

        # mode choices / quit

        singleplayer = Rectangle(Point(25, 200), Point(200, 300))
        sp_text = Text(Point(112.5, 250), "SINGLEPLAYER")
        sp_text.setFill('white')
        sp_text.draw(self.win)
        singleplayer.setOutline("white")
        self.structs.append(sp_text)
        self.structs.append(singleplayer)

        multiplayer = Rectangle(Point(300, 200), Point(475, 300))
        mp_text = Text(Point(387.5, 250), "MULTIPLAYER")
        mp_text.setFill('white')
        mp_text.draw(self.win)
        multiplayer.setOutline("white")
        self.structs.append(mp_text)
        self.structs.append(multiplayer)

        quit_button = Rectangle(Point(25, 400), Point(115, 475))
        quit_text = Text(Point(70, 437.5), "QUIT")
        quit_text.setFill('white')
        quit_button.setFill("red")
        self.structs.append(quit_button)
        self.structs.append(quit_text)

        singleplayer.draw(self.win)
        multiplayer.draw(self.win)
        quit_button.draw(self.win)
        quit_text.draw(self.win)

        while True:
            # listens to a mouse click in the areas encompassed by buttons
            click_point = self.win.getMouse()

            # modifies the game board structure accordingly
            if self.inside(click_point, singleplayer):
                self.game_mode = 0
                self.erase_board()
                self.draw_game_board()
                return

            elif self.inside(click_point, multiplayer):
                self.game_mode = 1
                self.erase_board()
                self.draw_game_board()
                return

            elif self.inside(click_point, quit_button):
                self.win.close()

    def inside(self, point, rectangle):
        """checks that the passed point is inside the specified rectangle
        :param point:
        :param rectangle:
        :return: true if the point is contained by @param rectangle, false otherwise
        """

        ll = rectangle.getP1()  # assume p1 is ll (lower left)
        ur = rectangle.getP2()  # assume p2 is ur (upper right)

        return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

    def draw_game_board(self):
        # checkered divisions in the board

        for i in range(1, self.board_size):
            horiz_grid = i * self.size / self.board_size

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

    def erase_tokens(self):
        for token in self.tokens_drawn:
            token.undraw()

    def erase_board(self):
        for i in self.structs:
            i.undraw()

    # maps a mouse click to an index in the game board
    @staticmethod
    def from_point_to_index(collection, coordinate):

        if coordinate >= collection[len(collection) - 1]:
            return -1

        i = 0

        while i < len(collection) and coordinate > collection[i]:
            print(coordinate)
            print(collection[0])
            i += 1
        return i
