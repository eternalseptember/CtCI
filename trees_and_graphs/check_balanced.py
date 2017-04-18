"""
Implement a function to check if a binary tree is balanced. For
the purposes of this question, a balanced tree is defined to be
a tree such that the heights of the two subtrees of any node
never differ by more than one.
"""


class Node:
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


def is_binary(head):
	left_height = get_height(head.left)
	right_height = get_height(head.right)

	diff = left_height - right_height

	if abs(diff) <= 1:
		return True
	else:
		return False


def get_height(head, height):
	if head is None:
		return 0

	return height


# testing
# false: unbalanced
node6 = Node(6)
node5 = Node(5, None, node6)
node4 = Node(4, None, node5)
node3 = Node(3, None, node4)
node2 = Node(2, None, node3)
node1 = Node(1, None, node2)
print(is_binary(node1))


# false: unbalanced
node1 = Node(1)
node2 = Node(2, None, node1)
node3 = Node(3)
node4 = Node(4, node3, node2)
node5 = Node(5)
node6 = Node(6, node5, node4)
print(is_binary(node6))


# true: balanced
node1 = Node(1)
node3 = Node(3)
node2 = Node(2, node1, node3)
node8 = Node(8)
node7 = Node(7, None, node8)
node5 = Node(5)
node6 = Node(6, node5, node7)
node4 = Node(4, node2, node6)
print(is_binary(node4))


# true: balanced
node1 = Node(1)
node2 = Node(2, node1)
print(is_binary(node2))




