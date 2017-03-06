"""
You have two numbers represented by a linked list, where each
node contains a single digit. The digits are stored in reverse
order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the
sum as a linked list.
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


def add_linked_list_digits(head1, head2):
	# convert each linked list to number representation
	total = 0
	return total



# total should be 62
value1 = [0, 1]  # 10
value2 = [2, 5]  # 52

head1 = None
head2 = None

for value in value1:
	head1 = add(head1, value)

for value in value2:
	head2 = add(head2, value)

total = add_linked_list_digits(head1, head2)
print(total)




