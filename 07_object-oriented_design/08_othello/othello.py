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
        init_board = [
            [None for col in range(8)] for row in range(8)
            ]

        # with white and black in center
        # len(mat) is row; len(mat[0]) is col
        return init_board


    def print_board(self):
        # show black as "X" and white as "O" for readibility?
        return None




