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

# testing

