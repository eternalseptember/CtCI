"""
T1 and T2 are two very large binary trees, with T1 much bigger than T2.
Create an algorithm to determine if T2 is a subtree of T1.

A tree T2 is a subtree of T1 if there exists a node in T1 such that the
subtree of n is identical to T2. THat is, if you cut off the tree at node
n, the two trees would be identical.
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
	# checks if tree_2 is a subtree of tree_1

	return False


# Tree 1: basic tree, no similarities
node_2 = Node(2)
node_12 = Node(12, node_2)
node_1 = Node(1)
node_7 = Node(7, node_1, node_12)
node_9 = Node(9)
node_5 = Node(5, node_9, node_7)
node_3 = Node(3)
node_11 = Node(11, node_3)
node_4 = Node(4, None, node_11)
tree_1_root = Node(8, node_5, node_4)

# test case 1: False
node_a = Node(5)
node_b = Node(4)
tree_2_root = Node(8, node_a, node_b)

result = check_subtree(tree_1_root, tree_2_root)
print(result)

# test case 2: True
node_a = Node(2)
node_b = Node(12, node_a)
node_c = Node(1)
tree_2_root = Node(7, node_c, node_b)

result = check_subtree(tree_1_root, tree_2_root)
print(result)





