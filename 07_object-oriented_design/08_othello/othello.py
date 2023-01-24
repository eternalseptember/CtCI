"""
Othello is played as follows: Each Othello piece is white on one side and black
on the other. When a piece is surrounded by its opponents on both the left and
right sides, or both the top and bottom, it is said to be captured and its
color is flipped. On your turn, you must capture at least one of your
opponent's pieces. The game ends when either user has no more valid moves. The
win is assigned to the person with the most pieces. Implement the object-
oriented design for Othello.
"""

# Diagonal flipping not implemented based on problem description.
# Assuming game rules are flipping are rows that are not broken by empty spaces
# or pieces of the same color.


class Player:
	def __init__(self, color, othello_game):
		# color is 'B' or 'W'
		self.color = color
		self.othello = othello_game


	def __str__(self):
		return str(self.color)


	def __repr__(self):
		return str(self.color)


	def test_piece(self, row, col):
		return self.othello.test_spot(row, col, self.color)


	def place_piece(self, row, col):
		return self.othello.place_piece(row, col, self.color)


	def pass_turn(self):
		return self.othello.check_pass_turn(self.color)


class Othello_Piece:
	def __init__(self, color):
		# color is 'B' or 'W'
		self.color = color


	def __str__(self):
		return str(self.color)


	def __repr__(self):
		return str(self.color)


	def flip(self):
		if self.color == 'W':
			self.color = 'B'
		elif self.color == 'B':
			self.color = 'W'


class Othello:
	from o_print import \
		print_board, print_playable_spots, print_move_checks, print_score, \
		print_game_state
	from o_check import is_valid, check_NS_EW
	from o_flip import flip_pieces, flip_NS_EW


	def __init__(self):
		self.board = self.init_game_board()
		self.playable_spots = []  # [(row, col)]
		self.players = self.init_players()
		self.active_player = 0  # 0 for black, 1 for white
		self.pieces_played = 0
		self.turns_passed = 0
		self.black_count = 0
		self.white_count = 0
		self.move_checks = {}


	def init_game_board(self):
		# 8x8 grid
		# len(board) is row; len(board[0]) is col
		init_board = [
			[None for col in range(8)] for row in range(8)
			]
		return init_board


	def init_players(self):
		black = Player('B', self)
		white = Player('W', self)
		return [black, white]


	def init_pieces(self):
		# White and black starting positions
		self.place_piece(3, 3, 'W', True)
		self.place_piece(3, 4, 'B', True)
		self.place_piece(4, 3, 'B', True)
		self.place_piece(4, 4, 'W', True)


	def begin_game(self, test=False):
		if not test:
			self.init_pieces()

		self.print_board()
		# active_player = self.active_player


		# PLAYER TURNS HERE.
		# exec(open("./test_game_1.py").read())
		# exec(open("./test_game_2.py").read())



		while not self.check_game_ends(str(self.players[self.active_player])):
			player_choice = self.player_turn(self.active_player)

			# Change player turns.
			if self.active_player == 0:
				self.active_player = 1
			elif self.active_player == 1:
				self.active_player = 0




		# When a player has no valid moves, that player passes their turn.
		# When both players have no more moves, the game ends.


		# Count the score only after the game has ended.
		# self.count_score()
		# self.print_score()

		# Printing game info to set up test
		print()
		print()
		self.print_game_state()


	def test_spot(self, row, col, color_placed):
		if (row, col) not in self.move_checks:
			valid_spot = self.is_valid(row, col, color_placed)
			self.move_checks[(row, col)] = valid_spot
		else:
			valid_spot = self.move_checks[(row, col)]

		return valid_spot



	def player_turn(self, player=0):
		# One player turn at at time.
		# Main game loop manages checks for passing turns or ending the game.
		self.move_checks.clear()
		active_player = self.players[player]
		self.active_player = player
		placed_a_piece = False
		passed_turn = False
		acceptable_choices = [0, 1, 2]

		while (not placed_a_piece) and (not passed_turn):
			# choose from testing a spot, playing a piece, or passing a turn
			player_choice = ''

			print('{0}: '.format(str(active_player)))

			# Prompt varies depending on whether turn can be passed.
			if 2 in acceptable_choices:
				print("Type... '0' to test a piece, '1' to play a piece, or '2' to pass the turn.")
			else:
				print("Type... '0' to test a piece or '1' to play a piece.")


			player_choice = input()
			player_choice = int(player_choice)  # Converts str to int.


			if player_choice == 0:
				row = int(input('Row: '))
				col = int(input('Col: '))

				test_result = active_player.test_piece(row, col)

				if test_result:
					print('{0}, {1} is a valid spot.'.format(row, col))
				else:
					print('{0}, {1} is an invalid spot.'.format(row, col))

			elif player_choice == 1:
				row = int(input('Row: '))
				col = int(input('Col: '))
				placed_a_piece = active_player.place_piece(row, col)

				if placed_a_piece:
					print('{0} placed on {1}, {2}.'
						.format(str(active_player), row, col))
				else:
					print('{0}, {1} is an invalid spot.')

			elif player_choice == 2:
				if 2 in acceptable_choices:
					passed_turn = active_player.pass_turn()

				# If player cannot pass the turn, then remove this option.
				if not passed_turn:
					print('Cannot pass turn.')
					acceptable_choices.remove(2)

		# Values to keep track of player turns gand game state.
		if passed_turn:
			return "Pass"
		else:
			return "Play"


	def place_piece(self, row, col, color_placed, init_board=False):
		#  Skip the rules checking if setting up the board.
		if init_board:
			if (row, col) in self.playable_spots:
				self.playable_spots.remove((row, col))

			self.board[row][col] = Othello_Piece(color_placed)
			self.pieces_played += 1
			self.check_adjacent_spots(row, col)
			return True

		# Check to see if location is valid.
		# Check if the next player has any valid moves.
		# Do not change player turns if it returns False.
		if self.is_valid(row, col, color_placed):
			# Steps to place a piece.
			self.playable_spots.remove((row, col))
			self.board[row][col] = Othello_Piece(color_placed)
			self.pieces_played += 1
			self.turns_passed = 0  # reset the counter for determining end game
			self.check_adjacent_spots(row, col)

			# Print board before piece is placed.
			print('{0} on ({1}, {2}).'.format(color_placed, row, col))
			self.print_board()

			# Flip pieces.
			self.flip_pieces(row, col, color_placed)

			# Print the board after the piece is placed.
			self.print_board()
			return True
		else:
			print('Invalid spot.')
			return False


	def check_adjacent_spots(self, row, col):
		# Update the list of valid spots to play.
		check_W = True
		check_E = True
		check_N = True
		check_S = True

		# Check when piece is placed on edge or corners.
		if row == 0:
			check_N = False
		elif row == 7:
			check_S = False

		if col == 0:
			check_W = False
		elif col == 7:
			check_E = False

		# Check and add to list of playable spots.
		if check_W:
			col_left = col - 1
			piece = self.board[row][col_left]
			if piece is None:
				if (row, col_left) not in self.playable_spots:
					self.playable_spots.append((row, col_left))
		if check_E:
			col_right = col + 1
			piece = self.board[row][col_right]
			if piece is None:
				if (row, col_right) not in self.playable_spots:
					self.playable_spots.append((row, col_right))
		if check_N:
			row_above = row - 1
			piece = self.board[row_above][col]
			if piece is None:
				if (row_above, col) not in self.playable_spots:
					self.playable_spots.append((row_above, col))
		if check_S:
			row_below = row + 1
			piece = self.board[row_below][col]
			if piece is None:
				if (row_below, col) not in self.playable_spots:
					self.playable_spots.append((row_below, col))


	def check_pass_turn(self, color_placed):
		for spot in self.playable_spots:
			if spot in self.move_checks:
				valid = self.move_checks[spot]
			else:
				row, col = (spot)
				valid = self.is_valid(row, col, color_placed)
				self.move_checks[(row, col)] = valid

			# If there's something playable at all, stop checking.
			if valid:
				break

		# If there's a valid move, return False
		if valid:
			self.turns_passed = 0
			return False
		else:
			self.turns_passed += 1
			return True


	def check_game_ends(self, color_placed):
		if self.pieces_played == 64:
			return True
		if self.turns_passed == 2:
			return True

		return False


	def count_score(self):
		# run this only after there are no more moves left
		# like when the board is empty
		for row in self.board:
			for piece in row:
				if piece is not None:
					if str(piece) == 'B':
						self.black_count += 1
					elif str(piece) == 'W':
						self.white_count += 1





