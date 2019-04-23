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
        check_W = False
    elif col >= 7:
        check_E = False


    if check_W:
        print('Check left for pieces to flip.')
        self.flip_NS_EW(row, col, color_placed, "row", col-1, -1, -1)

    if check_E:
        print('Check right for pieces to flip.')
        self.flip_NS_EW(row, col, color_placed, "row", col+1, 8, 1)

    if check_N:
        print('Check above for pieces to flip.')
        self.flip_NS_EW(row, col, color_placed, "col", row-1, -1, -1)

    if check_S:
        print('Check below for pieces to flip.')
        self.flip_NS_EW(row, col, color_placed, "col", row+1, 8, 1)


def flip_NS_EW(self, row, col, color_placed, check_dir, start, stop, step):
    # check_dir is "row" or "col"
    opp_color = False
    end_piece = False
    potential_flips = []  # (row, col)

    # WHAT IF POTENTIAL FLIPS DON'T ACTUALLY FLIP???

    # For each direction, list potential pieces that could be flipped.
    # Stop checking if adj spot is color_placed or line has an empty spot.
    # Only flip if opp_color is surrounded by color_placed in unbroken line.
    for position in range(start, stop, step):
        if check_dir == 'row':
            if step == -1:
                print('\tCheck left: ({0}, {1})'.format(row, position))
            elif step == 1:
                print('\tCheck right: ({0}, {1})'.format(row, position))

            piece = self.board[row][position]

        elif check_dir == 'col':
            if step == -1:
                print('\tCheck above: ({0}, {1})'.format(position, col))
            elif step == 1:
                print('\tCheck below: ({0}, {1})'.format(position, col))

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

                if check_dir == 'row':
                    potential_flips.append((row, position))
                elif check_dir == 'col':
                    potential_flips.append((position, col))

    if len(potential_flips) > 0:
        print('\tPotential flips: {0}'.format(potential_flips))

    # Flip pieces
    if opp_color and end_piece:
        for flip in potential_flips:
            flip_row, flip_col = flip
            piece = self.board[flip_row][flip_col]
            piece.flip()
    return None




