"""
Implement an NxN jigsaw puzzle. Design the data structures and explain
an algorithm to solve the puzzle. You can assume that you have a fitsWith
method which, when passed two puzzle edges, returns True if the two edges
belong together.
"""


class Puzzle_Piece():
    def __init__(self, piece_num, top_edge, right_edge, bottom_edge, left_edge):
        self.piece_num = piece_num
        # clock-wise
        self.top_edge = top_edge
        self.right_edge = right_edge
        self.bottom_edge = bottom_edge
        self.left_edge = left_edge


    def rotate_clockwise(self):
        old_top_edge = self.top_edge
        old_right_edge = self.right_edge
        old_bottom_edge = self.bottom_edge
        old_left_edge = self.left_edge

        self.top_edge = old_left_edge
        self.right_edge = old_top_edge
        self.bottom_edge = old_right_edge
        self.left_edge = old_bottom_edge


    def rotate_counterclockwise(self):
        old_top_edge = self.top_edge
        old_right_edge = self.right_edge
        old_bottom_edge = self.bottom_edge
        old_left_edge = self.left_edge

        self.top_edge = old_right_edge
        self.right_edge = old_bottom_edge
        self.bottom_edge = old_left_edge
        self.left_edge = old_top_edge


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


                print(piece_num, end='\t')
            print()



        # Shuffle and randomly rotate pieces.


        return puzzle_pieces


class Puzzle_Solution():
    def __init__(self, puzzle_size):
        self.puzzle_size = puzzle_size  # N
        self.solution = self.blank_puzzle_mat(puzzle_size)


    def blank_puzzle_mat(self, puzzle_size):
        # len(mat) is row; len(mat[0]) is col
        blank_mat = [[None for col in range(puzzle_size)] for row in range(puzzle_size)]
        return blank_mat


    def print_solution(self):
        # Prints the solution with pieces already placed.
        for row in self.solution:
            print(row)


    def fits_with(edge_1, edge_2):
        # return True if the two edges belong together
        return None






