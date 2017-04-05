"""
Write an algorithm to find the "next" node (i.e., in-order successor)
of a given node in a binary search tree. You may assume that each node
has a link to its parent.
"""


class Node:
	def __init__(self, data=None, left=None, right=None, prev=None):
		self.data = data
		self.left = left
		self.right = right
		self.prev = prev


def print_tree(head):
	if head.left is not None:
		print_tree(head.left)
	print(head)
	if head.right is not None:
		print_tree(head.right)


def next_node(head):
	# stuff here
	return None

# testing
node13 = Node(13)
node14 = Node(14, node13)
node13.prev = node14
node10 = Node(10, None, node14)
node4 = Node(4)
node7 = Node(7)
node6 = Node(6, node4, node7)
node4.prev = node6
node7.prev = node6
node1 = Node(1)
node3 = Node(3, node1, node6)
node1.prev = node3
node3.prev = node3
node8 = Node(8, node3, node10)



