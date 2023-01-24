"""
Describe how you could use a single array to implement three stacks.
"""


class ThreeStacks:
	def __init__(self):
		self.three_stack_arr = [None, None, None]
		self.stack_1_beg = 0  # bottom of stack
		self.stack_1_end = 0  # top of stack
		self.stack_2_beg = 1
		self.stack_2_end = 1
		self.stack_3_beg = 2
		self.stack_3_end = 2


	def push(self, item, stack_num):
		beg, end = self.stack_indexes(stack_num)

		if self.three_stack_arr[beg] is None:
			self.three_stack_arr[beg] = item
		else:
			self.three_stack_arr.insert(end+1, item)
			self.push_update_indexes(stack_num)


	def pop(self, stack_num):
		beg, end = self.stack_indexes(stack_num)
		
		if beg == end:
			if self.three_stack_arr[end] is not None:
				item = self.three_stack_arr[end]
				self.three_stack_arr[end] = None
				return item
			else:
				return None
		else:
			item = self.three_stack_arr.pop(end)
			self.pop_update_indexes(stack_num)
			return item


	def peek(self, stack_num):
		beg, end = self.stack_indexes(stack_num)
		return self.three_stack_arr[end]


	def is_empty(self, stack_num):
		beg, end = self.stack_indexes(stack_num)
		if ((end - beg) > 0) or (self.three_stack_arr[beg] is not None):
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


	def push_update_indexes(self, stack_num):
		if stack_num == 1:
			self.stack_1_end += 1
			self.stack_2_beg += 1
			self.stack_2_end += 1
			self.stack_3_beg += 1
			self.stack_3_end += 1
		elif stack_num == 2:
			self.stack_2_end += 1
			self.stack_3_beg += 1
			self.stack_3_end += 1
		elif stack_num == 3:
			self.stack_3_end += 1


	def pop_update_indexes(self, stack_num):
		if stack_num == 1:
			self.stack_1_end -= 1
			self.stack_2_beg -= 1
			self.stack_2_end -= 1
			self.stack_3_beg -= 1
			self.stack_3_end -= 1
		elif stack_num == 2:
			self.stack_2_end -= 1
			self.stack_3_beg -= 1
			self.stack_3_end -= 1
		elif stack_num == 3:
			self.stack_3_end -= 1


	def __str__(self):
		return str(self.three_stack_arr)

