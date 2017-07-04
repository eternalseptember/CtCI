"""
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.
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


def print_tree(head):
	if head.left is not None:
		print_tree(head.left)
	print(head)
	if head.right is not None:
		print_tree(head.right)


def create_minimal_tree(list_of_values):
	num_of_nodes = len(list_of_values)
	center_index = num_of_nodes // 2
	center_value = list_of_values[center_index]

	if num_of_nodes % 2 == 0:
		# even number of values

	else:
		# odd number of values


	# return head


def create_tree(list_of_values):
	# create a left tree and right tree



# testing
"""
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
head = None

for value in values:
	head = create_minimal_tree(head, value)
"""


# testing
values = [0, 1, 2]
head = create_minimal_tree(values)

print_tree(head)







