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


    def init_pieces(self):
        # White and black starting positions
        self.place_piece(3, 3, 'W')
        self.place_piece(3, 4, 'B')
        self.place_piece(4, 3, 'B')
        self.place_piece(4, 4, 'W')


    def place_piece(self, row, col, color_placed):
        # check if location is valid
        if self.board[row][col] is not None:
            # cannot place piece there, but don't change player turns
            return False
        else:
            self.board[row][col] = Othello_Piece(color_placed)
            # update black/white counts
            return True


    def begin_game(self):
        self.init_pieces()

        # black goes first
        # keep track of active player in case of invalid move
        # count the number pieces flipped
        # subtract from colors flipped

        return None


    def check_row(self, row, color_placed):
        # pieces to be flipped
        count = 0
        return count


    def check_col(self, color, color_placed):
        # pieces to be flipped
        count = 0
        return count


    def flip_pieces(self, color_placed):
        count = 0
        # flip pieces
        return count






