"""
Given a circular linked list, implement an algorithm that
returns the node at the beginning of the loop.
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


def detect_loop(head):
	nodes = []
	loop = False
	loop_node = None

	while loop is False:
		if (head is not None) and (head not in nodes):
			nodes.append(head)
			head = head.next
		else:
			loop_node = head
			loop = True

	return loop_node







