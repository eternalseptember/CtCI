"""
Implement a function to check if a binary tree is a binary search tree.
"""


class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def check_bst(head):
	if head.left is not None:
		if head.left.data > head.data:
			return False
		else:
			check_bst(head.left)

	if head.right is not None:
		if head.data >= head.right.data:
			return False
		else:
			check_bst(head.right)
	return True

