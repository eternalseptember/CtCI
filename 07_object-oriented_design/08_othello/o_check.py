# Functions to check board state.
# Meant to be imported into the main Othello class.


def is_valid(self, row, col, color_placed):
    # Check if the piece is placed in a playable spot.
    if (row, col) not in self.playable_spots:
        return False
    else:
        # Check if a piece can be flipped.
        #
        # Checking in every direction isn't really necessary.
        #
        flip_row = self.check_row(row, col, color_placed)
        flip_col = self.check_col(row, col, color_placed)

        return flip_row or flip_col


def check_row(self, row, col, color_placed):
    # Used to check if placement is valid.
    # row and col refer to the placement of the newly placed piece.
    # Return True if a piece can be flipped.
    if row == 0:
        flip_left = False
        flip_right = self.check_right(row, col, color_placed)
    elif row == 7:
        flip_left = self.check_left(row, col, color_placed)
        flip_right = False
    else:
        flip_right = self.check_right(row, col, color_placed)
        flip_left = self.check_left(row, col, color_placed)

    return flip_right or flip_left


def check_col(self, row, col, color_placed):
    # Used to check if placement is valid.
    # row and col refer to the placement of the newly placed piece.
    # Return True if a piece can be flipped.

    if col == 0:
        flip_above = False
        flip_below = self.check_below(row, col, color_placed)
    elif col == 7:
        flip_above = self.check_above(row, col, color_placed)
        flip_below = False
    else:
        flip_below = self.check_below(row, col, color_placed)
        flip_above = self.check_above(row, col, color_placed)

    return flip_above or flip_below


def check_left(self, row, col, color_placed):
    # used by the check_row function
    # If the piece was placed on the left edge...
    if col == 0:
        return False

    # If the piece was placed anywhere else...
    for position in range(col-1, -1, -1):
        piece = self.board[row][position]
        # is this right?
        if piece is None:
            return False
        else:
            if str(piece) == color_placed:
                continue
            else:
                # something can be flipped
                return True

    return False


def check_right(self, row, col, color_placed):
    # Used by the check_row function.
    # If the piece was placed on the right edge...
    if col == 7:
        return False

    # If the piece was placed anywhere else...
    for position in range(col+1, 8):
        piece = self.board[row][position]
        if piece is None:
            return False
        else:
            if str(piece) == color_placed:
                continue
            else:
                # Something can be flipped
                return True

    return False


def check_above(self, row, col, color_placed):
    # Used by the check_col function.
    # If a piece was placed on the top edge...
    if col == 0:
        return False

    # If the piece was placed anywhere else...
    for position in range(row-1, -1, -1):
        piece = self.board[position][col]
        # check the decrement...
        if piece is None:
            return False
        else:
            if str(piece) == color_placed:
                continue
            else:
                # something can be flipped
                return True

    return False


def check_below(self, row, col, color_placed):
    # Used by the check_col function.
    # If a piece was placed on the bottom edge...
    if col == 7:
        return False

    # If the piece was placed anywhere else...
    for position in range(row+1, 8):
        piece = self.board[position][col]
        if piece is None:
            return False
        else:
            if str(piece) == color_placed:
                continue
            else:
                # Something can be flipped
                return True

    return False

