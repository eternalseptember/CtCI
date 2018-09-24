"""
Implement an NxN jigsaw puzzle. Design the data structures and explain
an algorithm to solve the puzzle. You can assume that you have a fitsWith
method which, when passed two puzzle edges, returns True if the two edges
belong together.

This is the puzzle solver.
"""


from puzzle_piece import *


class Puzzle_Solution():
    def __init__(self, puzzle_size):
        self.puzzle_size = puzzle_size  # N
        self.solution = self.blank_puzzle_mat(puzzle_size)
        self.corner_pieces = []
        self.edge_pieces = []
        self.interior_pieces = []


    def blank_puzzle_mat(self, puzzle_size):
        # len(mat) is row; len(mat[0]) is col
        blank_mat = [[None for col in range(puzzle_size)] for row in range(puzzle_size)]
        return blank_mat


    def print_solution(self):
        # Prints the solution with pieces already placed.
        for row in self.solution:
            print(row)


    def solve_puzzle(self, unsolved_puzzle):
        # Sort corner, other, and interior pieces.
        while len(unsolved_puzzle.puzzle_pieces) > 0:
            piece = unsolved_puzzle.puzzle_pieces.pop()
            edges = 0

            if piece.top_edge is None:
                edges += 1
            if piece.right_edge is None:
                edges += 1
            if piece.bottom_edge is None:
                edges += 1
            if piece.left_edge is None:
                edges += 1

            if edges == 2:
                self.corner_pieces.append(piece)
            elif edges == 1:
                self.edge_pieces.append(piece)
            else:
                self.interior_pieces.append(piece)

        print('Corner pieces:')
        for piece in self.corner_pieces:
            print(piece)

        print()
        print('Edge pieces:')
        for piece in self.edge_pieces:
            print(piece)

        print()
        print('Interior pieces:')
        for piece in self.interior_pieces:
            print(piece)


    def fits_with(edge_1, edge_2):
        # return True if edges fit together		
        return None






