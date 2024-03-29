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
			queue.append(single_node.left)
		else:
			single_node.left = Node(data)
			return head

		if single_node.right is not None:
			queue.append(single_node.right)
		else:
			single_node.right = Node(data)
			return head


def find(head, target):
	# find a node based on values
	queue = [(None, head)]

	while len(queue) > 0:
		top_of_stack = queue.pop(0)
		parent_node, current_node = (top_of_stack)

		left_match = False
		right_match = False

		if (current_node.left is None) and (target.left is None):
			left_match = True
		elif (current_node.left is not None) and (target.left is not None):
			if (current_node.left.data == target.left.data):
				left_match = True

		if (current_node.right is None) and (target.right is None):
			right_match = True
		elif (current_node.right is not None) and (target.right is not None):
			if (current_node.right.data == target.right.data):
				right_match = True


		if (current_node.data == target.data) and (left_match is True) and (right_match is True):
			return True, current_node, parent_node
		else:
			if current_node.left is not None:
				queue.append((current_node, current_node.left))
			if current_node.right is not None:
				queue.append((current_node, current_node.right))


	return False, None, None


def get_random_node(head):
	from random import randrange

	list_of_nodes = []

	# fill list here
	queue = [head]
	while (len(queue) > 0):
		top_node = queue.pop(0)
		list_of_nodes.append(top_node)

		if top_node.left is not None:
			queue.append(top_node.left)
		if top_node.right is not None:
			queue.append(top_node.right)

	# get random node
	number_of_nodes = len(list_of_nodes)
	random_node_index = randrange(number_of_nodes)
	return list_of_nodes[random_node_index]





