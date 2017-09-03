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


def convert_to_linked_list(num):
	# convert num to a linked list with the digits stored in reverse order
	digit_list = [int(digit) for digit in str(num)]
	digit_list = digit_list[::-1]

	head = None
	for value in digit_list:
		head = add(head, value)

	return head


def add_linked_list_nums(head1, head2):
	# Not completely sure if this is a valid assumption, but
	# if either head is none, treat them as if they're zeros.
	if (head1 is None) and (head2 is None):
		return Node(0)
	elif (head1 is None):
		return head2
	elif (head2 is None):
		return head1


	# Setup
	first_digit = None
	current_digit = None
	carry_over = 0

	# Add
	column_sum = head1.data + head2.data
	if column_sum < 10:
		new_digit = column_sum
		carry_over = 0
	else:
		new_digit = column_sum
		carry_over = 1

	# if new_head is None, make a new head
	# else make a new node and attach as next digit
	if first_digit is None:
		first_digit = Node(new_digit)
		current_digit = first_digit


	# carry over adds 1 to the next value

	# if there is a final carry


	return first_digit


# Test cases
math_problems = [
				(10, 52),   # 62
				(99, 201),  # 300
				(999, 1),   # 1000
				(102, 899)  # 1002
				]

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

total = add_linked_list_nums(head1, head2)
print('Total in linked list: ', end=' ')
print_linked_list(total)
print()


# sum of different lengths and sum where final carry is the final digit
# 99 + 201 = 300
# 999 + 1 = 1000
# 102 + 899 = 1002





