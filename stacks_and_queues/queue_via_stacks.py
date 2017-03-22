"""
Implement a MyQueue class which implements a queue using two stacks.
"""


class MyQueue:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []


	def add(self, item):
		self.stack1.append(item)


	def remove(self):
		# move items to the second stack
		while len(self.stack1) > 1:
			item = self.stack1.pop()
			self.stack2.append(item)

		# the last item is reached
		remove_item = self.stack1.pop()

		# put the items back
		while len(self.stack2) > 0:
			item = self.stack2.pop()
			self.stack1.append(item)

		return remove_item


	def peek(self):
		return self.stack1[0]


	def is_empty(self):
		if len(self.stack1) > 0:
			return False
		else:
			return True


	def __str__(self):
		return str(self.stack1)


# testing
test_values = [9, 1, 8, 4, 5, 6, 3]
test_queue = MyQueue()

for value in test_values:
	test_queue.add(value)

print('Test queue: ', end=' ')
print(test_queue)

for i in range(7):
	item = test_queue.remove()
	print('item removed: {0}'.format(item))
	print('remaining queue: {0}'.format(test_queue))


