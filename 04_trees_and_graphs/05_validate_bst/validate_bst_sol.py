# Solution to the "validate bst" problem from the answer key.


class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def check_bst(head, min=None, max=None):
	# O(N) time, where N is the number of nodes in the tree.
	# O(log N) space on a balanced tree.
	# Up to O(log N) recursive calls on the stack up to the tree depth.
	if head is None:
		return True

	if (((min is not None) and (head.data <= min)) or
		((max is not None) and (head.data > max))):
		return False

	if ((check_bst(head.left, min, head.data) is False) or
		(check_bst(head.right, head.data, max) is False)):
		return False

	return True

