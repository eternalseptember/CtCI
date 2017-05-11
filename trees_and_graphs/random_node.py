"""
You are implementing a binary tree class from scratch which, in addition to
insert, find, and delete, has a method getRandomNode() which returns a random
node from the tree. All nodes should be equally likely to be chosen. Design
and implement an algorithm for getRandomNode, and explain how you would
implement the rest of the methods.
"""


class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def __str__(self):
		left = None
		right = None

		if self.left is not None:
			left = self.left.data
		if self.right is not None:
			right = self.right.data

		return 'data: {0}  left: {1}  right: {2}'.format(self.data, left, right)


def print_level_order(head):
	queue = [head]

	while len(queue) > 0:
		head_node = queue.pop(0)
		print(head_node)
		if head_node.left is not None:
			queue.append(head_node.left)
		if head_node.right is not None:
			queue.append(head_node.right)


def insert(head, data):
	if head is None:
		return Node(data)

	queue = [head]

	while len(queue) > 0:
		single_node = queue.pop(0)
		if single_node.left is not None:
			queue.append(head.left)
		else:
			single_node.left = Node(data)
			return head

		if single_node.right is not None:
			queue.append(head.right)
		else:
			single_node.right = Node(data)
			return head


def find(head, target):
	# return node
	return None


def delete(head, target):
	# return head?
	return None


def get_random_node(head):
	# return ranodm node
	return None


# testing
#values = [7, 5, 3, 8, 1, 8, 0, 2, 5, 2, 4]
values = [1, 2, 3, 4, 5, 6, 7, 8]
head = None

for value in values:
	head = insert(head, value)


print_level_order(head)


