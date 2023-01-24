"""
Implment an algorithm to delete a node in the middle (i.e., any node
but the first and last node, not necessarily the exact middle) of a
singly linked list, given only access to that node.
"""


class Node:
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node


def print_linked_list(head):
	print(head.data, end=' ')
	if head.next is not None:
		print_linked_list(head.next)


def add(head, value):
	new_node = Node(value)

	if head is None:
		return new_node, new_node

	if head.next is None:
		head.next = new_node
	else:
		next_node = head.next
		while next_node.next is not None:
			next_node = next_node.next
		next_node.next = new_node

	return head, new_node


def delete_node(node):
	# "Deletes" the node by copying the data from the next node
	while node.next is not None:
		node.data = node.next.data

		if node.next.next is None:
			node.next = None
		else:
			node = node.next


