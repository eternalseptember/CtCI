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


def bst_sequences(head):
	if head is None:
		return None

	possible_arrays = []
	# root is the very first value that must be in every array
	first_value = head.data
	# left and right might not be inserted in the same order
	

	return possible_arrays


# testing
node1 = Node(1)
node3 = Node(3)
node2 = Node(2, node1, node3)

results = bst_sequences(node2)
# results: {2, 1, 3}, {2, 3, 1}
print(results)



