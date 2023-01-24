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
		flip_W = self.check_NS_EW(row, col, color_placed, 'W')
		flip_E = self.check_NS_EW(row, col, color_placed, 'E')
		flip_N = self.check_NS_EW(row, col, color_placed, 'N')
		flip_S = self.check_NS_EW(row, col, color_placed, 'S')

		return flip_W or flip_E or flip_N or flip_S


def check_NS_EW(self, row, col, color_placed, direction):
	# Direction: 'W' (left), 'E' (right), 'N' (up), 'S' (down)
	if direction == 'W':  # Left
		if col <= 0:  # Piece was placed on left edge.
			return False

		start = col-1
		stop = -1
		step = -1

	elif direction == 'E':  # Right
		if col >= 7:  # Piece was placed on right edge.
			return False

		start = col+1
		stop = 8
		step = 1

	elif direction == 'N':  # Up
		if row <= 0:  # Piece was placed on the top edge.
			return False

		start = row-1
		stop = -1
		step = -1

	elif direction == 'S':  # Down
		if row >= 7:  # Piece was placed on the bottom edge.
			return False

		start = row+1
		stop = 8
		step = 1


	# Check to see if a piece can flip.
	opp_color = False
	check_row = ['W', 'E']
	check_col = ['N', 'S']

	for position in range(start, stop, step):
		if direction in check_row:
			piece = self.board[row][position]
		elif direction in check_col:
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




