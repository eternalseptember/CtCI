"""
Implementing the solution for first common ancestor problem.

Solution 1: With links to parents.
O(d) time, where d is the depth of the deeper node.
"""


class Node:
	def __init__(self, data=None, left=None, right=None, parent=None):
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent

	def __str__(self):
		data = self.data
		left = None
		right = None

		if self.left is not None:
			left = self.left.data
		if self.right is not None:
			right = self.right.data

		return 'node: {0}  left: {1}  right: {2}'.format(data, left, right)


def common_ancestor(node1, node2):
	delta = depth(node1) - depth(node2)

	if delta > 0:
		first = node2  # shallower node
		second = node1  # deeper node
	else:
		first = node1
		second = node2

	second = go_up_by(second, abs(delta))  # move deeper node up

	# Find where paths intersect
	while ((first is not None) and (second is not None) and (first != second)):
		first = first.parent
		second = second.parent

	if (first is None) or (second is None):
		return None
	else:
		return first


def go_up_by(node, delta):
	while (node is not None) and (delta > 0):
		node = node.parent
		delta -= 1
	return node


def depth(node):
	depth = 0

	while node is not None:
		node = node.parent
		depth += 1

	return depth








