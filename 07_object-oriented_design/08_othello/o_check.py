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
        flip_left = self.check_row(row, col, color_placed, "W")
        flip_right = self.check_row(row, col, color_placed, "E")
        flip_below = self.check_below(row, col, color_placed)
        flip_above = self.check_above(row, col, color_placed)

        return flip_left or flip_right or flip_above or flip_below


def check_row(self, row, col, color_placed, direction):
    # Direction: "W" (left) or "E" (right)
    if direction == "W":  # Left
        if col <= 0:  # Piece was placed on left edge.
            return False

        start = col-1
        stop = -1
        step = -1

    elif direction == "E":  # Right
        if col >= 7:  # Piece was placed on right edge.
            return False

        start = col+1
        stop = 8
        step = 1

    opp_color = False

    for position in range(start, stop, step):
        piece = self.board[row][position]

        if piece is None:
            return False
        else:
            if str(piece) == color_placed:
                if opp_color:
                    return True
                else:
                    return False
            else:
                if opp_color is False:
                    opp_color = True

    return False


def check_above(self, row, col, color_placed):
    # If a piece was placed on the top edge...
    if col <= 0:
        return False

    # If the piece was placed anywhere else...
    opp_color = False

    for position in range(row-1, -1, -1):
        piece = self.board[position][col]

        if piece is None:
            return False
        else:
            if str(piece) == color_placed:
                if opp_color:
                    return True
                else:
                    return False
            else:
                if opp_color is False:
                    opp_color = True

    return False


def check_below(self, row, col, color_placed):
    # If a piece was placed on the bottom edge...
    if col >= 7:
        return False

    # If the piece was placed anywhere else...
    opp_color = False

    for position in range(row+1, 8):
        piece = self.board[position][col]

        if piece is None:
            return False
        else:
            if str(piece) == color_placed:
                if opp_color:
                    return True
                else:
                    return False
            else:
                if opp_color is False:
                    opp_color = True

    return False

