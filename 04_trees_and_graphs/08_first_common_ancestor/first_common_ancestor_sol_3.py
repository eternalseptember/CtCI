"""
Implementing the solution for first common ancestor problem.

Solution 3: Without links to parents.

Follow a chain in which p and q are on the same side.
If both are on the left or right side of the node,
branch in that direction to look for the common ancestor.
Common ancestor is found when p and q are no longer on the same side.


covers is called on 2n nodes in the first call:
	n nodes for the left side and
	n nodes for the right side.

Then the algorithm branches left or right, where
covers will be called on (2n/2) nodes, then (2n/4) nodes, etc.,
resulting in O(n) time on a balanced tree.
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


def common_ancestor(root, p, q):
	# Error check - one node is not in the tree.
	if (not covers(root, p)) or (not covers(root, q)):
		return None

	return ancestor_helper(root, p, q)


def ancestor_helper(root, p, q):
	if (root is None) or (root == p) or (root == q):
		return root

	p_is_left = covers(root.left, p)
	q_is_left = covers(root.left, q)

	# nodes are on different sides
	if p_is_left is not q_is_left:
		return root

	if p_is_left:
		child_side = root.left
	else:
		child_side = root.right

	return ancestor_helper(child_side, p, q)


def covers(root, p):
	if root is None:
		return None
	if root == p:
		return True

	return covers(root.left, p) or covers(root.right, p)




