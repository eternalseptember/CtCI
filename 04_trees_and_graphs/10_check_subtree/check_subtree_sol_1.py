# Simple approach: check substring
# Time: O(n + m)
# Space: O(n + m)
# n = nodes in tree 1; m = nodes in tree 2


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


def pre_order(root, seq):
	if root is None:
		seq.append('X')
		return

	seq.append(root.data)

	pre_order(root.left, seq)
	pre_order(root.right, seq)
	return seq


def pre_order_str(seq):
	res = pre_order(seq, [])
	res_str = ' '.join(str(val) for val in res)
	return res_str


def check_subtree(tree_1, tree_2):
	# checks if tree_2 is a subtree of tree_1
	res1 = pre_order_str(tree_1)
	res2 = pre_order_str(tree_2)

	return res2 in res1









