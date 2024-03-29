"""
T1 and T2 are two very large binary trees, with T1 much bigger than T2.
Create an algorithm to determine if T2 is a subtree of T1.

A tree T2 is a subtree of T1 if there exists a node in T1 such that the
subtree of n is identical to T2. THat is, if you cut off the tree at node
n, the two trees would be identical.
"""


class Node():
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


def check_subtree(tree_1, tree_2):
	# checks if tree_2 is a subtree of tree_1

	if tree_2 is None:
		return True
	if tree_1 is None:
		return False

	tree_1_main_queue = [tree_1]

	while len(tree_1_main_queue) > 0:
		tree_1_node = tree_1_main_queue.pop(0)
		tree_2_node = tree_2
		tree_1_queue = []
		tree_2_queue = []

		while is_matching(tree_1_node, tree_2_node):

			if tree_1_node.left is not None:
				tree_1_queue.append(tree_1_node.left)
			if tree_1_node.right is not None:
				tree_1_queue.append(tree_1_node.right)

			if tree_2_node.left is not None:
				tree_2_queue.append(tree_2_node.left)
			if tree_2_node.right is not None:
				tree_2_queue.append(tree_2_node.right)

			if (len(tree_1_queue) == 0) and (len(tree_2_queue) == 0):
				return True
			else:
				tree_1_node = tree_1_queue.pop(0)
				tree_2_node = tree_2_queue.pop(0)


		if tree_1_node.left is not None:
			tree_1_main_queue.append(tree_1_node.left)
		if tree_1_node.right is not None:
			tree_1_main_queue.append(tree_1_node.right)


	return False


def is_matching(node_1, node_2):
	left_match = False
	right_match = False

	if (node_1.left is None) and (node_2.left is None):
		left_match = True
	elif (node_1.left is not None) and (node_2.left is not None):
		if node_1.left.data == node_2.left.data:
			left_match = True

	if (node_1.right is None) and (node_2.right is None):
		right_match = True
	elif (node_1.right is not None) and (node_2.right is not None):
		if node_1.right.data == node_2.right.data:
			right_match = True

	if (node_1.data == node_2.data) and left_match and right_match:
		return True
	else:
		return False









