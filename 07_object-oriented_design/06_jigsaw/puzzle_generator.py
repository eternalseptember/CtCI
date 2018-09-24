# Generates puzzle to be solved.


from puzzle_piece import *
import random


class Puzzle():
    def __init__(self, size):
        self.size = size
        self.puzzle_pieces = self.generate_puzzle(size)


    def generate_puzzle(self, size):
        # Assumes size is at least 2.
        # Pieces are numbered from 1 to (size * size).
        puzzle_pieces = []

        for row in range(1, size+1):
            for col in range(1, size+1):
                piece_num = (row-1) * size + col

                # Define default edges.
                left_edge = piece_num - 1
                right_edge = piece_num + 1
                top_edge = piece_num - size
                bottom_edge = piece_num + size

                # Define edge pieces.
                if col == 1:  # left edge piece
                    left_edge = None
                elif col == size:  # right edge piece
                    right_edge = None
                if row == 1:  # top edge piece
                    top_edge = None
                elif row == size:  # bottom edge piece
                    bottom_edge = None

                piece = Puzzle_Piece(
                    piece_num,
                    top_edge,
                    right_edge,
                    bottom_edge,
                    left_edge
                    )

                puzzle_pieces.append(piece)

        # Shuffle and randomly rotate pieces.
        random.shuffle(puzzle_pieces)

        for piece in puzzle_pieces:
            rand = random.randint(1, 4)

            # 1: stay the same
            # 2: rotate clockwise
            # 3: rotate counter-clockwise
            # 4: rotate twice for upside-down
            if rand == 2:
                piece.rotate_clockwise()
            elif rand == 3:
                piece.rotate_counterclockwise()
            elif rand == 4:
                piece.rotate_clockwise()
                piece.rotate_clockwise()

        return puzzle_pieces


    def print_pieces(self):
        for piece in self.puzzle_pieces:
            print(piece)


