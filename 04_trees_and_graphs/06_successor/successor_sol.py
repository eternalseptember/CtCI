# Solution to the "successor" problem from the answer key.


class Node:
	def __init__(self, data=None, left=None, right=None, prev=None):
		self.data = data
		self.left = left
		self.right = right
		self.prev = prev

	def __str__(self):
		left = None
		right = None
		prev = None

		if self.left is not None:
			left = self.left.data
		if self.right is not None:
			right = self.right.data
		if self.prev is not None:
			prev = self.prev.data

		d_str = '{0}'.format(self.data).rjust(4)
		l_str = '{0}'.format(left).rjust(4)
		r_str = '{0}'.format(right).rjust(4)
		p_str = '{0}'.format(prev).rjust(4)

		return 'data: {0}    left: {1}    right: {2}    prev: {3}'.format(d_str, l_str, r_str, p_str)


def print_tree(head):
	if head.left is not None:
		print_tree(head.left)
	print(head)
	if head.right is not None:
		print_tree(head.right)


def find_next_node(head):
	if head is None:
		return None

	# Found right children -> return left-most node of right subtree
	if head.right is not None:
		return left_most_child(head.right)
	else:
		# some assignments
		current_node = head
		parent_node = current_node.prev

		# go up until we're on left instead of right
		while ((parent_node is not None) and (parent_node.left is not current_node)):
			current_node = parent_node
			parent_node = parent_node.prev

		return parent_node

	return None


def left_most_child(head):
	if head is None:
		return None

	while head.left is not None:
		head = head.left

	return head

