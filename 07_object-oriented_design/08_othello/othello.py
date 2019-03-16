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
        if self.board[row][col] is not None:
            # A piece is already in this position.
            return False
        elif not self.is_valid(row, col, color_placed):
            # Not a valid position for whatever reasons.
            return False
        else:
            self.board[row][col] = Othello_Piece(color_placed)
            self.pieces_played += 1
            return True


    def is_valid(self, row, col, color_placed):
        # piece placement is valid if a piece can be flipped
        # and must be adjacent to existing pieces?
        return None


    def check_left(self, row, col, color_placed):
        # used by the check_row function
        return None


    def check_right(self, row, col, color_placed):
        # used by the check_row function
        for col in range(1, 8):
            piece = self.board[row][col]
            if piece is None:
                return False
            else:
                # what color is the piece?
                print('stuff')

        # return True if there is a piece that can be flipped.
        return None


    def check_row(self, row, col, color_placed):
        # Used to check if placement is valid.
        # row and col refer to the placement of the new piece.
        # Return True if a piece can be flipped.

        if row == 0:
            flip = self.check_right(row, col, color_placed)

        elif row == 7:
            # Only check to the left.
            print('only check left')
        else:
            # Check in both directions
            print('check both')
        return None


    def check_col(self, row, col, color_placed):
        # used to check if placement is valid
        # return True if a piece can be flipped
        # check up and down
        # don't check further up if row == 0
        # don't check further down if row == 7
        return None


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


    def print_score(self):
        print("Final Score")
        print("Black: {0}".format(self.black_count))
        print("White: {0}".format(self.white_count))






