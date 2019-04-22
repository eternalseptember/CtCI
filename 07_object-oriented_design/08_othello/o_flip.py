# Function for flipping pieces.
# Meant to be imported into the main Othello class.


def flip_pieces(self, row, col, color_placed):
    check_W = True
    check_E = True
    check_N = True
    check_S = True

    # Check when piece is placed on edge or corners.
    if row <= 0:
        check_N = False
    elif row >= 7:
        check_S = False

    if col <= 0:
        check_W = Falsse
    elif col >= 7:
        check_E = False

    # For each direction, list potential pieces that could be flipped.
    # Stop checking if adj spot is color_placed or line has an empty spot.
    # Only flip if opp_color is surrounded by color_placed in unbroken line.
    if check_W:
        self.flip_NS_EW(row, col, color_placed, "row", col-1, -1, -1)

    if check_E:
        self.flip_NS_EW(row, col, color_placed, "row", col+1, 1, 1)

    if check_N:
        self.flip_NS_EW(row, col, color_placed, "col", row-1, -1, -1)

    if check_S:
        self.flip_NS_EW(row, col, color_placed, "col", row+1, 1, 1)


def flip_NS_EW(self, row, col, color_placed, check_dir, start, stop, step):
    # check_dir is "row" or "col"
    opp_color = False
    end_piece = False
    potential_flips = []  # (row, col)

    # Check
    for position in range(start, stop, step):
        if check_dir == "row":
            piece = self.board[row][position]
        elif check_dir == "col":
            piece = self.board[position][col]

        if piece is None:
            break
        else:
            if str(piece) == color_placed:
                if opp_color:
                    end_piece = True
                break
            else:
                if opp_color is False:
                    opp_color = True
                potential_flips.append((row, position))

    # Flip pieces
    if opp_color and end_piece:
        for flip in potential_flips:
            flip_row, flip_col = flip
            piece = self.board[flip_row][flip_col]
            piece.flip()
    return None




