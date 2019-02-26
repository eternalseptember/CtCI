"""
Othello is played as follows: Each Othello piece is white on one side and black
on the other. When a piece is surrounded by its opponents on both the left and
right sides, or both the top and bottom, it is said to be captured and its
color is flipped. On your turn, you must capture at least one of your
opponent's pieces. The game ends when either user has no more valid moves. The
win is assigned to the person with the most pieces. Implement the object-
oriented design for Othello.
"""


class Othello:
    def __init__(self):
        self.board = self.init_game_board()


    def init_game_board(self):
        # 8x8 grid
        # len(board) is row; len(board[0]) is col
        init_board = [
            [None for col in range(8)] for row in range(8)
            ]

        # White and black starting positions
        init_board[3][3] = 'W'
        init_board[3][4] = 'B'
        init_board[4][3] = 'B'
        init_board[4][4] = 'W'

        return init_board


    def print_board(self):
        # show black as "X" and white as "O" for readibility?
        for row in self.board:
            for piece in row:
                print('{0}  '.format(piece))
            print()




