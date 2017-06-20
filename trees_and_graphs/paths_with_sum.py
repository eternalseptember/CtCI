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
	nodes_in_current_path = []
	# could backtrack once a leaf has been visited


	# let's start at the root
	current_node = head
	sum_of_current_path += current_node.data
	nodes_in_current_path.append(current_node)


	if current_node.left is not None:
		current_node = current_node.left
		sum_of_current_path += current_node.data
		nodes_in_current_path.append(current_node)

		if sum_of_current_path == value:
			paths.append(nodes_in_current_path)



	return len(paths)




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



