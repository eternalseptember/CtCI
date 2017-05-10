"""
You are implementing a binary tree class from scratch which, in addition to
insert, find, and delete, has a method getRandomNode() which returns a random
node from the tree. All nodes should be equally likely to be hcosen. Design
and implement an algorithm for getRandomNode, and explain how you would
implement the rest of the methods.
"""


class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


	def insert(self, head, data):
		if head is None:
			return Node(data)
		if head.left is None:
			head.left = Node(data)
			return head
		if head.right is None:
			head.right = Node(data)
			return head


		# don't think this is a min or max heap
		queue = []


		return head


	def find(self, target):
		# return node
		return None


	def delete(self, target):
		# return head?
		return None


	def get_random_node(self):
		# return ranodm node
		return None


# testing

