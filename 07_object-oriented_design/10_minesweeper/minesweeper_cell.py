# Each cell in a minesweeper board.


class Cell():
	def __init__(self, is_mine=False, num_of_adj_mines=0, is_revealed=False):
		self.is_mine = is_mine
		self.num_of_adj_mines = num_of_adj_mines
		self.is_revealed = is_revealed
		self.flagged = False


	def __str__(self):
		if self.is_revealed:
			if self.is_mine:
				return 'X'
			else:
				if self.num_of_adj_mines == 0:
					return str(' ')
				else:
					return str(self.num_of_adj_mines)
		elif self.flagged:
			return '!'
		else:
			return '-'



	def __repr__(self):
		if self.is_revealed:
			if self.is_mine:
				return 'X'
			else:
				if self.num_of_adj_mines == 0:
					return str(' ')
				else:
					return str(self.num_of_adj_mines)
		elif self.flagged:
			return '!'
		else:
			return '-'


	def export_format(self):
		return '({0},{1},{2})'\
			.format(self.is_mine, self.num_of_adj_mines, self.is_revealed)


	def set_mine(self):
		self.is_mine = True

	def add_adj_mine(self):
		self.num_of_adj_mines += 1

	def num_in_cell(self):
		return self.num_of_adj_mines

	def is_blank(self):
		# Returns the opposite of reveal().
		# Use this function to NOT mess with the is_revealed count.
		return (not self.is_mine) and (self.num_of_adj_mines == 0)

	def reveal(self):
		self.is_revealed = True

		# Returns the opposite of is_blank().
		if self.is_mine or (self.num_of_adj_mines > 0):
			return True
		else:
			return False

	def flag(self):
		self.flagged = True

	def unflag(self):
		self.flagged = False


