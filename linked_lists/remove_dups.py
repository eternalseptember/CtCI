"""
Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?
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


def remove_next_node(head):
	# terminal base cases
	if head is None:
		return None
	if head.next is None:
		return head

	# remove head.next
	if head.next.next is None:
		head.next = None
	else:
		head.next = head.next.next

	return head



def remove_duplicates(head):
	# this implementation uses a temporary buffer
	unique_values = []
	current_head = head
	previous = Node()

	while current_head is not None:
		if current_head in unique_values:
			previous.next = current_head.next
		else:
			unique_values.append(current_head)
			previous = current_head

		current_head = current_head.next

	return head



"""
def remove_duplicates(head):
	# this implementation does not use a temporary buffer
	# Runs in O(1) space but O(N^2) time.
	current_node = head

	while current_node is not None:
		this_node = current_node

		while this_node.next is not None:
			if this_node.next.data == current_node.data:
				this_node = remove_next_node(this_node)
			else:
				this_node = this_node.next

		current_node = current_node.next

	return head
"""

# Setup for testing
values = [9, 0, 1, 1, 9, 3, 4, 2, 0, 2, 5, 1]
head = None

for value in values:
	head = add(head, value)

print('linked list adding all nodes:')
print_linked_list(head)
print()

head = remove_duplicates(head)
print('linked list after removing duplicates:')
print_linked_list(head)
print()
