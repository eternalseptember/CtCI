# Puzzle pieces to be used by the puzzle generator and solver.


class Puzzle_Piece():
	def __init__(self, piece_num, top_edge, right_edge, bottom_edge, left_edge):
		# Order of edges defined: clock-wise
		# Correct puzzle solution
		self.piece_num = piece_num
		self.top_edge = top_edge
		self.right_edge = right_edge
		self.bottom_edge = bottom_edge
		self.left_edge = left_edge


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


