"""
Design an algorithm to write code to find the first common ancestor of two
nodes in a binary tree. Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.
"""


class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def common_ancestor(node1, node2):
	# return something


# testing
node9 = Node(9)
node1 = Node(1)
node2 = Node(2)
node12 = Node(12, node2)
node7 = Node(7, node1, node12)
node5 = Node(5, node9, node7)
node3 = Node(3)
node11 = Node(11, node3)
node4 = Node(4, None, node11)
node8 = Node(8, node5, node4)



