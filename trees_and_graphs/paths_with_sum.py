"""
You are given a binary tree in which each node contains an integer value
(which might be positive or negative). Design an algorithm to count the
number of paths that sum to a given value. The path does not need to
start or end at the root or a leaf, but it must go downwards (traveling
only from parent nodes to child nodes).
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


def count_paths(head, value):
	# return number of paths that sum to a given value
	paths = []

	sum_of_current_path = 0

	list_of_paths = get_list_of_paths(head)


	return len(paths)


def get_list_of_paths(head):
	paths_list = get_path(head)

	"""
	for item in paths_list:
		print(item)
	"""

	return paths_list


def get_path(head, current_path=[]):
	if head is not None:
		current_path.append(head)

	if (head.left is None) and (head.right is None):
		for item in current_path:
			print(item)
		print()
		return current_path
	if (head.left is not None):
		get_path(head.left, current_path)
	if (head.right is not None):
		get_path(head.right, current_path)

	return current_path





# Binary Tree 1
node_a = Node(-1)
node_b = Node(5)
node_c = Node(-11)
node_d = Node(4)
node_e = Node(2, None, node_a)
node_f = Node(6, node_b, node_c)
node_g = Node(9, node_d)
node_h = Node(7, node_e, node_f)
node_i = Node(5, None, node_g)
node_j = Node(-2, node_h, node_i)

total_sum = 14
num_of_paths = count_paths(node_j, total_sum)
print(num_of_paths)



