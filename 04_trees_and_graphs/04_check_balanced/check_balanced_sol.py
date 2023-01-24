# More efficient approach from the answer key.
# O(N) time and O(H) space, where H is the height of the tree.


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
	if get_height(head) is False:
		return False
	else:
		return True


def get_height(head):
	if head is None:
		return -1

	left_height = get_height(head.left)
	if left_height is False:
		return False

	right_height = get_height(head.right)
	if right_height is False:
		return False

	height_diff = left_height - right_height
	if abs(height_diff) > 1:
		return False
	else:
		return max(left_height, right_height) + 1

