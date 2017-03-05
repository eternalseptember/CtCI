"""
Implement an algorithm to find the kth to last element of a singly linked list.
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


def find_element(k, head):
	items = []

	while head.next is not None:
		items.append(head.data)
		head = head.next

	if len(items) < k:
		return None
	else:
		return items[-k]


values = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
head = None

for value in values:
	head = add(head, value)

print('linked list adding all nodes:')
print_linked_list(head)
print()

k = 2
result = find_element(k, head)
print('{0}-to-last element in linked list:'.format(k))
print(result)



