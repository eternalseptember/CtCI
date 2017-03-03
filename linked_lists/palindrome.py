"""
Implement a function to check if a linked list is a palindrome.
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


def is_palindrome(head):
	string = []
	return True



values = ['r', 'a', 'c', 'e', 'c', 'a', 'r']
head = None

for value in values:
	head = add(head, value)

print('linked list adding all nodes:')
print_linked_list(head)
print()

result = is_palindrome(head)
print(result)


