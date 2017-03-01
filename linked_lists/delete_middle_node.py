"""
Implment an algorithm to delete a node in the middle (i.e., any node
but the first and last node, not necessarily the exact middle) of a
singly linked list, given only access to that node.
"""


class Node:
	# def __init__(self, data=None, prev=None, next_node=None):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node


def print_linked_list(head):
	print(head.data, end=' ')
	if head.next is not None:
		print_linked_list(head.next)


def add(head, value):
	if head is None:
		return Node(value)

	if head.next is None:
		head.next = Node(value)
	else:
		next_node = head.next
		while next_node.next is not None:
			next_node = next_node.next
		next_node.next = Node(value)

	return head


def delete_node(node):
	if node is None:
		return
	while node.next is not None:
		node.data = node.next.data
		node = node.next
	if node.next is None:
		node.data is None
		node.next is None



# Setup for testing
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
head = None
delete_this_node = None

for value in values:
	head = add(head, value)

	# set a value for testing
	if value == 4:
		delete_this_node = head

print('linked list adding all nodes:')
print_linked_list(head)
print()


delete_node(delete_this_node)
print('linked list after deleting a middle node:')
print_linked_list(head)
print()

