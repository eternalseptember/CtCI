"""
Alternative approach: search through the larger tree, T1.
Every time a node in T1 matches the root of T2, call match_tree.

Worse case runtime: O(nm), where
n is the number of nodes in T1 and
m is the number of nodes in T2.

More accurate runtime: O(n + km), where
k is the number of times T2's root is in T1.
But matchtree exits when there's a difference between trees.

Space: O(log(n) + log(m))

More optimal in terms of space, and likely to be more optimal in time.
Depends on whether to reduce average case runtime at the expense of
worst case runtime.
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
	if tree_2 is None:
		return True  # The empty tree is always a subtree.

	return subtree(tree_1, tree_2)


def subtree(tree_1, tree_2):
	if tree_1 is None:
		return False  # Big tree empty and subtree not found.
	elif (tree_1.data == tree_2.data) and match_tree(tree_1, tree_2):
		return True
	return subtree(tree_1.left, tree_2) or subtree(tree_1.right, tree_2)


def match_tree(tree_1, tree_2):
	if (tree_1 is None) and (tree_2 is None):
		return True  # Nothing left in subtree.
	elif (tree_1 is None) or (tree_2 is None):
		return False  # One tree is empty, therefore trees don't match.
	elif tree_1.data != tree_2.data:
		return False  # Data doesn't match.
	else:
		return match_tree(tree_1.left, tree_2.left) and match_tree(tree_1.right, tree_2.right)







