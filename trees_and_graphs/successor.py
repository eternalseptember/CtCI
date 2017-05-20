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
	if head.right is not None:
		next_node = head.right

		if next_node.left is not None:
			return next_node.left
		else:
			return next_node

	else:
		# there's no right node
		if head.prev is None:
			# root node
			return None
		else:
			# go up the tree
			return head.prev



# test tree. in-order: 1, 3, 4, 6, 7, 8, 10, 13, 14
node13 = Node(13)
node14 = Node(14, node13)
node13.prev = node14
node10 = Node(10, None, node14)
node14.prev = node10

node4 = Node(4)
node7 = Node(7)
node6 = Node(6, node4, node7)
node4.prev = node6
node7.prev = node6

node1 = Node(1)
node3 = Node(3, node1, node6)
node1.prev = node3
node6.prev = node3

node8 = Node(8, node3, node10)
node3.prev = node8
node10.prev = node8

#print_tree(node8)

# test case 1: node10
next_node = find_next_node(node8)
print(next_node)

# test case 2: node13
next_node = find_next_node(node10)
print(next_node)

# test case 3: node14
next_node = find_next_node(node13)
print(next_node)

