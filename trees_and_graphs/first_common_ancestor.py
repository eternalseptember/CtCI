"""
Design an algorithm to write code to find the first common ancestor of two
nodes in a binary tree. Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.
"""


class Node:
	def __init__(self, data=None, left=None, right=None, parent=None):
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent


def common_ancestor(node1, node2):
	node_behind = node1

	while node_behind.parent is not None:
		node_ahead = node2
		# look for parent node

		node_behind = node_behind.parent



# testing
node9 = Node(9)
node1 = Node(1)
node2 = Node(2)
node12 = Node(12, node2)
node2.parent = node12
node7 = Node(7, node1, node12)
node1.parent = node7
node12.parent = node7
node5 = Node(5, node9, node7)
node9.parent = node5
node7.parent = node5
node3 = Node(3)
node11 = Node(11, node3)
node3.parent = node11
node4 = Node(4, None, node11)
node11.parent = node4
node8 = Node(8, node5, node4)
node5.parent = node8
node4.parent = node8


# test 1: node8
ancestor = common_ancestor(node5, node4)


