"""
Othello is played as follows: Each Othello piece is white on one side and black
on the other. When a piece is surrounded by its opponents on both the left and
right sides, or both the top and bottom, it is said to be captured and its
color is flipped. On your turn, you must capture at least one of your
opponent's pieces. The game ends when either user has no more valid moves. The
win is assigned to the person with the most pieces. Implement the object-
oriented design for Othello.
"""

# Diagonal flipping not implemented based on problem description.


class Player:
    def __init__(self, color, othello_game):
        # color is 'B' or 'W'
        self.color = color
        self.othello = othello_game

    def place_piece(self, row, col):
        self.othello.place_piece(row, col, self.color)


class Othello_Piece:
    def __init__(self, color):
        # color is 'B' or 'W'
        self.color = color


    def __str__(self):
        return str(self.color)


    def flip(self):
        if self.color == 'W':
            self.color = 'B'
        elif self.color == 'B':
            self.color = 'W'


class Othello:
    def __init__(self):
        self.board = self.init_game_board()
        self.valid_spots = []  # [(row, col)]
        self.init_players = self.init_players()
        self.pieces_played = 0
        self.black_count = 0
        self.white_count = 0


    def print_board(self):
        for row in self.board:
            for piece in row:
                if piece is None:
                    print('_  ', end=' ')
                else:
                    print('{0}  '.format(piece), end=' ')
            print()


    def print_score(self):
        print("Final Score")
        print("Black: {0}".format(self.black_count))
        print("White: {0}".format(self.white_count))


    def init_game_board(self):
        # 8x8 grid
        # len(board) is row; len(board[0]) is col
        init_board = [
            [None for col in range(8)] for row in range(8)
            ]
        return init_board


    def init_players(self):
        black = Player('B', self)
        white = Player('W', self)
        return [black, white]


    def init_pieces(self):
        # White and black starting positions
        self.place_piece(3, 3, 'W', True)
        self.place_piece(3, 4, 'B', True)
        self.place_piece(4, 3, 'B', True)
        self.place_piece(4, 4, 'W', True)


    def begin_game(self):
        self.init_pieces()

        # black goes first
        # keep track of active player in case of invalid move
        # function to check if the current player has a valid move to make
        # switch player turn

        # Count the score only after the game has ended.
        self.count_score()
        self.print_score()


    def place_piece(self, row, col, color_placed, init_board=False):
        #  Skip the rules checking if setting up the board.
        if init_board:
            self.board[row][col] = Othello_Piece(color_placed)
            self.pieces_played += 1
            return True

        # Check if location is valid.
        # Do not change player turns if it returns False.
        # Check if the next player has any valid moves.
        if self.board[row][col] is not None:
            # A piece is already in this position.
            return False
        elif not self.is_valid(row, col, color_placed):
            # Not a valid position for whatever reasons.
            return False
        else:
            self.board[row][col] = Othello_Piece(color_placed)
            self.pieces_played += 1
            #
            # REMOVE THIS LOCATION FROM LIST OF VALID SPOTS
            # ADD NEW ONES
            #
            return True


    def update_board(self, row, col, color_placed):
        # flip pieces *because a move is valid if pieces can be flipped*
        return None


    def flip_piece(self, row, col):
        piece = self.board[row][col]
        piece.flip()


    def count_score(self):
        # run this only after there are no more moves left
        # like when the board is empty
        for row in self.board:
            for piece in row:
                if piece is not None:
                    if str(piece) == 'B':
                        self.black_count += 1
                    elif str(piece) == 'W':
                        self.white_count += 1


    def is_valid(self, row, col, color_placed):
        if (row, col) not in self.valid_spots:
            return False
        else:
            # Check if a piece can be flipped.
            flip_row = self.check_row(row, col, color_placed)
            flip_col = self.check_col(row, col, color_placed)

            return flip_row or flip_col


    def check_adjacent_spots(self, row, col):
        #
        # USE THIS TO UPDATE self.valid_spots
        #
        check_left = True
        check_right = True
        check_above = True
        check_below = True

        # check when piece is placed on edge or corners
        if row == 0:
            check_above = False
        elif row == 7:
            check_below = False

        if col == 0:
            check_left = False
        elif col == 7:
            check_right = False


        if check_left:
            piece = self.board[row][col-1]
            if piece is None:
                if (row, col) not in self.valid_spots:
                    self.valid_spots.append((row, col))
        if check_right:
            piece = self.board[row][col+1]
            if piece is None:
                if (row, col) not in self.valid_spots:
                    self.valid_spots.append((row, col))
        if check_above:
            piece = self.board[row-1][col]
            if piece is None:
                if (row, col) not in self.valid_spots:
                    self.valid_spots.append((row, col))
        if check_below:
            piece = self.board[row+1][col]
            if piece is None:
                if (row, col) not in self.valid_spots:
                    self.valid_spots.append((row, col))


    def check_row(self, row, col, color_placed):
        # Used to check if placement is valid.
        # row and col refer to the placement of the new piece.
        # Return True if a piece can be flipped.
        if row == 0:
            flip_left = False
            flip_right = self.check_right(row, col, color_placed)
        elif row == 7:
            flip_left = self.check_left(row, col, color_placed)
            flip_right = False
        else:
            flip_right = self.check_right(row, col, color_placed)
            flip_left = self.check_left(row, col, color_placed)

        return flip_right or flip_left


    def check_col(self, row, col, color_placed):
        # Used to check if placement is valid.
        # row and col refer to the placement of the new piece.
        # Return True if a piece can be flipped.

        if col == 0:
            flip_above = False
            flip_below = self.check_below(row, col, color_placed)
        elif col == 7:
            flip_above = self.check_above(row, col, color_placed)
            flip_below = False
        else:
            flip_below = self.check_below(row, col, color_placed)
            flip_above = self.check_above(row, col, color_placed)

        return flip_above or flip_below


    def check_left(self, row, col, color_placed):
        # used by the check_row function
        # If the piece was placed on the left edge...
        if col == 0:
            return False

        # If the piece was placed anywhere else...
        for position in range(col-1, -1, -1):
            piece = self.board[row][position]
            # is this right?
            if piece is None:
                return False
            else:
                if str(piece) == color_placed:
                    continue
                else:
                    # something can be flipped
                    return True

        return False


    def check_right(self, row, col, color_placed):
        # Used by the check_row function.
        # If the piece was placed on the right edge...
        if col == 7:
            return False

        # If the piece was placed anywhere else...
        for position in range(col+1, 8):
            piece = self.board[row][position]
            if piece is None:
                return False
            else:
                if str(piece) == color_placed:
                    continue
                else:
                    # Something can be flipped
                    return True

        return False


    def check_above(self, row, col, color_placed):
        # Used by the check_col function.
        # If a piece was placed on the top edge...
        if col == 0:
            return False

        # If the piece was placed anywhere else...
        for position in range(row-1, -1, -1):
            piece = self.board[position][col]
            # check the decrement...
            if piece is None:
                return False
            else:
                if str(piece) == color_placed:
                    continue
                else:
                    # something can be flipped
                    return True

        return False


    def check_below(self, row, col, color_placed):
        # Used by the check_col function.
        # If a piece was placed on the bottom edge...
        if col == 7:
            return False

        # If the piece was placed anywhere else...
        for position in range(row+1, 8):
            piece = self.board[position][col]
            if piece is None:
                return False
            else:
                if str(piece) == color_placed:
                    continue
                else:
                    # Something can be flipped
                    return True

        return False






