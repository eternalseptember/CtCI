# Option 6
# O(log N), where N is the number of nodes.


from random import *


class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
		self.size = 1


	def get_random_node(self):
		if self.left is None:
			left_size = 0
		else:
			left_size = self.left.size

		# Java's nextInt(n) returns a random number
		# between 0 (inclusive) and n (exclusive).
		# randint in inclusive for both boundaries.
		random_index = randint(0, self.size-1)

		# Testing
		"""
		print('Current node:\n\t', end='')
		print(self)
		print('Random index: {0}'.format(random_index))
		"""

		if random_index < left_size:
			return self.left.get_random_node()
		elif random_index == left_size:
			return self
		else:
			return self.right.get_random_node()


	def insert_in_order(self, item):
		if item <= self.data:
			if self.left is None:
				self.left = Node(item)
			else:
				self.left.insert_in_order(item)
		else:
			if self.right is None:
				self.right = Node(item)
			else:
				self.right.insert_in_order(item)

		self.size += 1


	def find(self, item):
		if item == self.data:
			return self
		elif item <= self.data:
			if self.left is not None:
				return self.left.find(item)
			else:
				return None
		elif item > self.data:
			if self.right is not None:
				return self.right.find(item)
			else:
				return None
		return None


	def __str__(self):
		left = None
		right = None

		if self.left is not None:
			left = self.left.data
		if self.right is not None:
			right = self.right.data

		return 'data: {0}  left: {1}  right: {2}  size: {3}'\
			.format(self.data, left, right, self.size)


def print_tree(head):
	queue = [head]

	while len(queue) > 0:
		head_node = queue.pop(0)
		print(head_node)
		if head_node.left is not None:
			queue.append(head_node.left)
		if head_node.right is not None:
			queue.append(head_node.right)






