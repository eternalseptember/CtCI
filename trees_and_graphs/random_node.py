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
		# insert node at next available spot, then swap
		return head


	def find(self, target):
		# return node
		return None


	def delete(self, target):
		# return head?
		return None


	def get_random_node(self):
		# return ranodm node


