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
		return 'data: {0}  left: {1}  right: {2}'.format(self.data, self.left, self.right)




# testing
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

node1 = Node(1)
print(node1)



