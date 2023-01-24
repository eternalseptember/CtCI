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

	# root is the very first value that must be in every array
	beg_sequence = [head.data]

	if (head.left is None) and (head.right is None):
		return beg_sequence

	# finds the possible sequences of left and right subtrees
	left = None
	right = None

	if head.left is not None:
		left = bst_sequences(head.left)
	if head.right is not None:
		right = bst_sequences(head.right)

	# creates all possible sequences for entire tree
	possible_sets = []

	if right is None:
		# left only
		possible_sets.append(left)
	elif left is None:
		# right only
		possible_sets.append(right)
	else:
		# ltr
		possible_sets.append(left + right)
		# rtl
		possible_sets.append(right + left)


	# prepend the beg_sequence
	all_possible_sets = []

	for each_set in possible_sets:

		new_seq = beg_sequence + each_set
		all_possible_sets.append(new_seq)

	return all_possible_sets







