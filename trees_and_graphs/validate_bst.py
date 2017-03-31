"""
Implement a function to check if a binary tree is a binary search tree.
"""


class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def check_bst(head):
	#
	return True



# testing: true
node1 = Node(1)
node4 = Node(4)
node7 = Node(7)
node6 = Node(6, node4, node7)
node3 = Node(3, node1, node6)
node13 = Node(13)
node14 = Node(14, node13)
node10 = Node(10, None, node14)
node8 = Node(8, node3, node10)

result1 = check_bst(head8)

# testing: false
node2 = Node(2)
node1 = Node(1)
node9 = Node(9)
node12 = Node(12, node2)
node7 = Node(7, node1, node12)
node5 = Node(5, node9, node7)
node3 = Node(3)
node11 = Node(11, node3)
node4 = Node(4, None, node11)
node8 = Node(8, node5, node4)

result2 = check_bst(node8)

print('{0}  {1}'.format(result1, result2))


