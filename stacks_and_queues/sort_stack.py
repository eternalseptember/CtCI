"""
Write a program to sort a stack such that the smallest items are on top.
You can use an additional temporary stack, but you may not copy the
elements into any other data structure (such as array). The stack supports
the following operations: push, pop, peek, and isEmpty().
"""

class Stack:
	def __init__(self):
		self.stack = []


	def push(self, item):
		self.stack.append(item)


	def pop(self):
		item = self.stack.pop()
		return item


	def peek(self):
		return self.stack[0]


	def is_empty(self):
		if len(self.stack) > 0:
			return False
		else:
			return True


def sort(unsorted_stack):
	# larger items are at the bottom
	temp_stack = Stack()
	temp_item = None

	# first pass to find the largest item
	while unsorted_stack.is_empty() is False:
		item = unsorted_stack.pop()

		if temp_item is None:
			temp_item = item
		elif item > temp_item:
			temp_stack.push(temp_item)
			temp_item = item
		else:
			temp_stack.push(item)


# testing
values_to_add = [1, 2, 7, 5, 9, 0, 3, 2, 7, 6, 6, 8]

stack = Stack()
for value in values_to_add:
	stack.push(value)



