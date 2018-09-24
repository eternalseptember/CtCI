"""
Implement an NxN jigsaw puzzle. Design the data structures and explain
an algorithm to solve the puzzle. You can assume that you have a fitsWith
method which, when passed two puzzle edges, returns True if the two edges
belong together.
"""


import random


class Puzzle_Piece():
    def __init__(self, piece_num, top_edge, right_edge, bottom_edge, left_edge):
        # Order of edges defined: clock-wise
        # Correct puzzle solution
        self.piece_num = piece_num
        self.top_edge = top_edge
        self.right_edge = right_edge
        self.bottom_edge = bottom_edge
        self.left_edge = left_edge

        # Status of each pieces' connections as puzzle is being solved.
        # 'None' means that side is an edge.
        # 'False' means side is not an edge, and is available for connection.
        # When a connection is made, it points to the next piece.
        self.top = False
        self.right = False
        self.bottom = False
        self.left = False

        if self.top_edge is None:
            self.top = None
        if self.right_edge is None:
            self.right = None
        if self.bottom_edge is None:
            self.bottom = None
        if self.left is None:
            self.left = None

        is_connected_to_another_piece = False  # used for rotating


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


    def __str__(self):
        summary = ''
        summary += 'Piece: {0}\t\t'.format(self.piece_num)
        summary += 'Top: {0}\t\t'.format(self.top_edge)
        summary += 'Right: {0}\t\t'.format(self.right_edge)
        summary += 'Bottom: {0}\t\t'.format(self.bottom_edge)
        summary += 'Left: {0}'.format(self.left_edge)
        return summary


    def __repr__(self):
        summary = ''
        summary += 'Piece: {0}\t\t'.format(self.piece_num)
        summary += 'Top: {0}\t\t'.format(self.top_edge)
        summary += 'Right: {0}\t\t'.format(self.right_edge)
        summary += 'Bottom: {0}\t\t'.format(self.bottom_edge)
        summary += 'Left: {0}'.format(self.left_edge)
        return summary


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


    def fits_with(piece_1, piece_2):
            if (piece_1.piece_num == piece_2.top_edge) or \
                (piece_1.piece_num == piece_2.right_edge) or \
                (piece_1.piece_num == piece_2.bottom_edge) or \
                (piece_1.piece_num == piece_2.left_edge):

                # connect the pieces
                # align pieces for left-right or top-bottom connection
                if piece_1.top == piece_2.piece_num:
                    edge_1 = top
                elif piece_1.right == piece_2.piece_num:
                    edge_1 = right
                elif piece_1.bottom == piece_2.piece_num:
                    edge_1 = bottom
                elif piece_1.left == piece_2.piece_num:
                    edge_1.left

                return True
            else:
                return False






