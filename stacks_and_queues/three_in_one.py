"""
Describe how you could use a single array to implement three stacks.
"""


class ThreeStacks:
	def __init__(self):
		self.three_stack_arr = []
		self.stack_1_beg = 0 # bottom of stack
		self.stack_1_end = 0 # top of stack
		self.stack_2_beg = 1
		self.stack_2_end = 1
		self.stack_3_beg = 2
		self.stack_3_end = 2

	def push(self, item, stack_num):
		# recalculate indexes

	def pop(self, stack_num):
		# get the top item
		# recalculate indexes

	def peek(self, stack_num):
		beg, end = self.stack_indexes(stack_num)
		try:
			return self.three_stack_arr[end]
		else:
			return None

	def is_empty(self, stack_num):
		beg, end = self.stack_indexes(stack_num)
		if (end - beg) > 0:
			return False
		else:
			return True


	def stack_indexes(self, stack_num):
		if stack_num == 1:
			return self.stack_1_beg, self.stack_1_end
		elif stack_num == 2:
			return self.stack_2_beg, self.stack_2_end
		elif stack_num == 3:
			return self.stack_3_beg, self.stack_3_end
		else:
			return None




