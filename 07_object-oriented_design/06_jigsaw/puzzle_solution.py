"""
Implement an NxN jigsaw puzzle. Design the data structures and explain
an algorithm to solve the puzzle. You can assume that you have a fitsWith
method which, when passed two puzzle edges, returns True if the two edges
belong together.

This is the puzzle solver.
"""


from collections import deque


class Puzzle_Solution():
    def __init__(self, puzzle_size):
        self.puzzle_size = puzzle_size  # N
        self.solution = self.blank_puzzle_mat(puzzle_size)
        self.corner_pieces = []
        self.edge_pieces = deque()
        self.interior_pieces = deque()


    def blank_puzzle_mat(self, puzzle_size):
        # len(mat) is row; len(mat[0]) is col
        blank_mat = [
            [None for col in range(puzzle_size)] for row in range(puzzle_size)
            ]
        return blank_mat


    def print_sorted_pieces(self):
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


    def print_solution(self):
        # Prints the solution with pieces already placed.
        for row in self.solution:
            for col in row:
                try:
                    print('{0:>4}'.format(col.piece_num), end=' ')
                except AttributeError:
                    print('None', end=' ')
            print()


    def print_piece_details(self):
        for row in self.solution:
            for col in row:
                print(col)


    def solve_puzzle(self, unsolved_puzzle):
        self.sort_pieces(unsolved_puzzle)
        self.place_corner_pieces()
        self.place_edge_pieces()

        # place interior pieces





        print('puzzle solved')



    def fits_with(self, placed_piece, edge):
        if edge == placed_piece:
            return True
        else:
            return False


    def sort_pieces(self, unsolved_puzzle):
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


    def place_corner_pieces(self):
        # Going to pretend that corner pieces can be clearly identified,
        # as if the corners are unique and that looking at the box art will
        # yield the correct placement.
        max_dim = self.puzzle_size - 1  # maximum array size

        while len(self.corner_pieces) > 0:
            piece = self.corner_pieces.pop()

            if piece.piece_num == 1:
                # Top left corner
                if (piece.bottom_edge is None):
                    if (piece.right_edge is None):
                        piece.rotate_clockwise()
                    piece.rotate_clockwise()
                else:
                    if (piece.right_edge is None):
                        piece.rotate_counterclockwise()

                self.solution[0][0] = piece

            elif piece.piece_num == self.puzzle_size:
                # Top right corner
                if (piece.bottom_edge is None):
                    if (piece.left_edge is None):
                        piece.rotate_counterclockwise()
                    piece.rotate_counterclockwise()
                else:
                    if (piece.left_edge is None):
                        piece.rotate_clockwise()

                self.solution[0][max_dim] = piece

            elif piece.piece_num == (self.puzzle_size * self.puzzle_size):
                # Bottom right corner
                if (piece.top_edge is None):
                    if (piece.left_edge is None):
                        piece.rotate_clockwise()
                    piece.rotate_clockwise()
                else:
                    if (piece.left_edge is None):
                        piece.rotate_counterclockwise()

                self.solution[max_dim][max_dim] = piece

            else:
                # Bottom left corner
                if (piece.top_edge is None):
                    if (piece.right_edge is None):
                        piece.rotate_counterclockwise()
                    piece.rotate_counterclockwise()
                else:
                    if (piece.right_edge is None):
                        piece.rotate_clockwise()

                self.solution[max_dim][0] = piece


    def place_edge_pieces(self):
        # Solving edge pieces.
        max_dim = self.puzzle_size - 1  # maximum array size

        # Going clockwise, starting with the top-left corner:
        row = 0
        col = 0

        while len(self.edge_pieces) > 0:
            placed_piece = self.solution[row][col]

            # Where is the next spot?
            if (row == 0):
                if col == max_dim:
                    # Top-right corner going down
                    row += 1
                else:
                    # Top-left corner going right
                    col += 1

            elif(row == max_dim):
                if col == 0:
                    # Bottom-left corner going up
                    row -= 1
                else:
                    # Bottom-right corner going left
                    col -= 1

            else:
                if (col == max_dim):
                    # Top-right going down
                    row += 1
                elif (col == 0):
                    # Bottom-left going up
                    row -= 1


            # Testing traveling along the edge clockwise.
            # Checks to see if the next spot is empty:
            while self.solution[row][col] is None:
                edge_piece = self.edge_pieces.popleft()


                if row == 0:
                    while edge_piece.top_edge is not None:
                        edge_piece.rotate_clockwise()
                    edge = edge_piece.left_edge

                elif row == max_dim:
                    while edge_piece.bottom_edge is not None:
                        edge_piece.rotate_clockwise()
                    edge = edge_piece.right_edge

                elif col == 0:
                    while edge_piece.left_edge is not None:
                        edge_piece.rotate_clockwise()
                    edge = edge_piece.bottom_edge

                elif col == max_dim:
                    while edge_piece.right_edge is not None:
                        edge_piece.rotate_clockwise()
                    edge = edge_piece.top_edge


                piece_fits = self.fits_with(placed_piece.piece_num, edge)


                if piece_fits:
                    self.solution[row][col] = edge_piece
                else:
                    self.edge_pieces.append(edge_piece)




