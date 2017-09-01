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
	num1 = convert_to_int(head1)
	num2 = convert_to_int(head2)
	total = num1 + num2

	# then converts the answer to a linked list in the same format
	return convert_to_linked_list(total)


def convert_to_int(head):
	# converts the linked list representation to an integer
	digits = []

	while head is not None:
		digits.insert(0, head.data)
		head = head.next

	digit_str = ''
	for digit in digits:
		digit_str += str(digit)

	return int(digit_str)


def convert_to_linked_list(num):
	# convert num to a linked list with the digits stored in reverse order
	digit_list = [int(digit) for digit in str(num)]
	digit_list = digit_list[::-1]

	head = None
	for value in digit_list:
		head = add(head, value)

	return head


# total should be 62
value1 = 10
value2 = 52

head1 = convert_to_linked_list(value1)
print('Value 1: {0}\nLinked List: '.format(value1), end=' ')
print_linked_list(head1)
print('\n')

head2 = convert_to_linked_list(value2)
print('Value 2: {0}\nLinked List: '.format(value2), end=' ')
print_linked_list(head2)
print('\n')

total = add_linked_list_digits(head1, head2)
print('Total in linked list: ', end=' ')
print_linked_list(total)
print()





