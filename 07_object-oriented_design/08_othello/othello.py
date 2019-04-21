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
# Assuming game rules are flipping are rows that are not broken by empty spaces
# or pieces of the same color.


class Player:
    def __init__(self, color, othello_game):
        # color is 'B' or 'W'
        self.color = color
        self.othello = othello_game

    def place_piece(self, row, col):
        self.othello.place_piece(row, col, self.color)


    def __str__(self):
        return str(self.color)


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
    from o_print import print_board, print_playable_spots, print_score
    from o_check import is_valid, check_NS_EW
    from o_flip import flip_pieces, flip_NS_EW


    def __init__(self):
        self.board = self.init_game_board()
        self.playable_spots = []  # [(row, col)]
        self.players = self.init_players()
        self.pieces_played = 0
        self.black_count = 0
        self.white_count = 0


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
        self.print_board()  # Print updated board after each turn.

        # black goes first
        active_player = self.players[0]
        print(active_player)
        # keep track of active player in case of invalid move
        # function to check if the current player has a valid move to make
        # switch player turn

        self.print_playable_spots()
        can_put_a_piece_here = self.is_valid(2, 3, 'B')
        print(can_put_a_piece_here)

        # Count the score only after the game has ended.
        self.count_score()
        self.print_score()


    def place_piece(self, row, col, color_placed, init_board=False):
        #  Skip the rules checking if setting up the board.
        if init_board:
            if (row, col) in self.playable_spots:
                self.playable_spots.remove((row, col))

            self.board[row][col] = Othello_Piece(color_placed)
            self.pieces_played += 1
            self.check_adjacent_spots(row, col)
            return True

        # Check to see if location is valid.
        # Check if the next player has any valid moves.
        # Do not change player turns if it returns False.
        if self.is_valid(row, col, color_placed):
            self.playable_spots.remove((row, col))
            self.board[row][col] = Othello_Piece(color_placed)
            self.pieces_played += 1
            self.check_adjacent_spots(row, col)
            # FLIP PIECES
            return True
        else:
            return False


    def check_adjacent_spots(self, row, col):
        # Update the list of valid spots to play.
        check_W = True
        check_E = True
        check_N = True
        check_S = True

        # Check when piece is placed on edge or corners.
        if row == 0:
            check_N = False
        elif row == 7:
            check_S = False

        if col == 0:
            check_W = False
        elif col == 7:
            check_E = False

        # Check and add to list of playable spots.
        if check_W:
            col_left = col - 1
            piece = self.board[row][col_left]
            if piece is None:
                if (row, col_left) not in self.playable_spots:
                    self.playable_spots.append((row, col_left))
        if check_E:
            col_right = col + 1
            piece = self.board[row][col_right]
            if piece is None:
                if (row, col_right) not in self.playable_spots:
                    self.playable_spots.append((row, col_right))
        if check_N:
            row_above = row - 1
            piece = self.board[row_above][col]
            if piece is None:
                if (row_above, col) not in self.playable_spots:
                    self.playable_spots.append((row_above, col))
        if check_S:
            row_below = row + 1
            piece = self.board[row_below][col]
            if piece is None:
                if (row_below, col) not in self.playable_spots:
                    self.playable_spots.append((row_below, col))


    def check_game_ends(self, color_placed):
        if self.pieces_played == 64:
            return True
        # when neither player can make a move
        return None


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





