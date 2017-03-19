"""
How would you design a stack which, in addition to push and pop,
has a function min which returns the minimum element? Push, pop,
and min should all operate in O(1) time.
"""


class Stack:
	def __init__(self):
		self.stack = []
		self.min_item = None


	def push(self, item):
		self.stack.append(item)

		if self.min_item is None:
			self.min_item = item
		else:
			if item < self.min_item:
				self.min_item = item


	def pop(self):
		item = self.stack.pop()

		if item == self.min_item:
			if len(self.stack) > 0:
				self.min_item = min(self.stack)
			else:
				self.min_item = None

		return item


	def peek(self):
		return self.stack[-1]


	def is_empty(self):
		if len(self.stack) > 0:
			return False
		else:
			return True


	def print_min(self):
		print(self.min_item)


# test
values_to_add = [5, 6, 1, 2, 8, 0, 9]

new_stack = Stack()
for value in values_to_add:
	new_stack.push(value)
	new_stack.print_min()


