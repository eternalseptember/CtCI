"""
A binary search tree was created by traversing through an array from
left to right and inserting each element. Given a binary search tree
with distinct elements, print all possible arrays that could have led
to this tree.
"""


class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def bst_sequences(head, prev_sequences=[]):
	if head is None:
		return None

	# root is the very first value that must be in every array
	prev_sequences.append(head.data)

	if head.left is None and head.right is None:
		return prev_sequences

	all_sets = []
	left = None
	right = None

	if head.left is not None:
		left = bst_sequences(head.left, prev_sequences)

	if head.right is not None:
		right = bst_sequences(head.right, prev_sequences)

	if (left is not None) and (right is not None):
		ltr = []
		rtl = []

	return all_sets




# testing: {2, 1, 3}, {2, 3, 1}
node1 = Node(1)
node3 = Node(3)
node2 = Node(2, node1, node3)

results = bst_sequences(node2)
print(results)

"""
# testing: 
node4 = Node(4)
node1 = Node(1, node4)
node3 = Node(3)
node2 = Node(2, node1, node3)

results = bst_sequences(node2)
print(results)
"""



