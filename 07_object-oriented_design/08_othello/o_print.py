# Functions that print the state of the game.
# Meant to be imported into the main Othello class.


def print_board(self):
	for row in range(8):
		for col in range(8):
			piece = self.board[row][col]
			if piece is None:
				if (row, col) in self.playable_spots:
					print(' - ', end='')
				else:
					print(' . ', end='')
			else:
				print(' {0} '.format(piece), end='')
		print()

	print("*****************************************")


def print_playable_spots(self):
	print('PIECES PLAYED: {0}'.format(self.pieces_played))
	print('PLAYABLE SPOTS:', end=' ')
	for spot in self.playable_spots:
		print(spot, end=' ')
	print()


def print_move_checks(self):
	# color placed?
	for spot in self.move_checks:
		is_valid = self.move_checks[spot]
		print('    {0}: {1}'.format(spot, is_valid))
	# print()



def print_score(self):
	print("************** FINAL SCORE **************")
	print("Black: {0}".format(self.black_count))
	print("White: {0}".format(self.white_count))


def print_game_state(self):
	# For setting up the game state so that the later stages of the game is
	# easier to test.
	print('GAME STATE')

	# self.board
	print("*****************************************")
	self.print_board()

	# need to remember whose turn it is
	print('PLAYER TURN: {0}'.format(self.active_player))

	# self.pieces_played
	# self.playable_spots
	self.print_playable_spots()

	# self.move_checks
	print('MOVE CHECKS:')
	self.print_move_checks()

	# self.turns_passed
	print('TURNS PASSED: {0}'.format(self.turns_passed))


	# self.black_count
	# self.white_count
	self.count_score()
	self.print_score()




