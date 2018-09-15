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


class Puzzle():
    def __init__(self, size):
        self.size = size

    def generate_puzzle(self):
        # Create sample puzzle.
        # Number of pieces = n * n.
        # Shuffle pieces.
        return None


class Puzzle_Solution():
    def __init__(self, puzzle_size):
        self.puzzle_size = puzzle_size  # N
        self.solution = self.blank_puzzle_mat(puzzle_size)


    def blank_puzzle_mat(self, puzzle_size):
        # len(mat) is row; len(mat[0]) is col
        blank_mat = [[0 for i in range(puzzle_size)] for i in range(puzzle_size)]
        return blank_mat


    def print_solution(self):
        # Prints the solution with pieces already placed.
        for row in self.solution:
            print(row)


    def fits_with(edge_1, edge_2):
        # return True if the two edges belong together
        return None






