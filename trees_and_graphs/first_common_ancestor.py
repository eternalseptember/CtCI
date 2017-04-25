"""
Design an algorithm to write code to find the first common ancestor of two
nodes in a binary tree. Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.
"""


class Node:
	def __init__(self, data=None, left=None, right=None, parent=None):
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent


def common_ancestor(node1, node2):

	# assumes that only one of the nodes can be the root node
	if node1.parent is None:
		node_ahead = node1
		node_behind = node2
	elif node2.parent is None:
		node_ahead = node2
		node_behind = node1



		
	else:
		# neither of the nodes are the root
		node_ahead = node2
		node_behind = node1

		while node_behind.parent is not None:
			parent_1 = node_behind.parent
			node_ahead = node2
			
			while node_ahead.parent is not None:
				parent_2 = node_ahead.parent

				if (parent_1.data == parent_2.data) and (parent_1.left == parent_2.left) and (parent_1.right == parent_2.right):
						return parent_2


				node_ahead = node_ahead.parent

			node_behind = node_behind.parent

	return None


# test 1: node 8
node9 = Node(9)
node1 = Node(1)
node2 = Node(2)
node12 = Node(12, node2)
node2.parent = node12
node7 = Node(7, node1, node12)
node1.parent = node7
node12.parent = node7
node5 = Node(5, node9, node7)
node9.parent = node5
node7.parent = node5
node3 = Node(3)
node11 = Node(11, node3)
node3.parent = node11
node4 = Node(4, None, node11)
node11.parent = node4
node8 = Node(8, node5, node4)
node5.parent = node8
node4.parent = node8

ancestor = common_ancestor(node5, node4)
print('ancestor node: {0}  left: {1}  right: {2}'.format(ancestor.data, ancestor.left.data, ancestor.right.data))



# test 2: node 2
node1 = Node(1)
node3 = Node(3)
node2 = Node(2, node1, node3)
node1.parent = node2
node3.parent = node3

ancestor = common_ancestor(node1, node3)
print('ancestor node: {0}  left: {1}  right: {2}'.format(ancestor.data, ancestor.left.data, ancestor.right.data))


# test 3: one node is higher than the other



