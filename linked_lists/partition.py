"""
Write code to partition a linked list around a value x, such that
all nodes less than x come before all nodes greater than or equal
to x. If x is contained within the list, the values of x only need
to be after the elements less than x. The partition element x can
appear anywhere in the "right partition"; it does not need to
appear between the left and right partitions.
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


def partition(head, x):
	left_head = None
	left_tail = None
	right_head = None
	right_tail = None

	while head is not None:
		next_node = head.next
		head.next = None

		if head.data < x:
			# stick it in the left partition
			if left_head is None:
				left_head = head
				left_tail = left_head
			else:
				left_tail.next = head
				left_tail = head
		else:
			# stick it in the right partition
			if right_head is None:
				right_head = head
				right_tail = right_head
			else:
				right_tail.next = head
				right_tail = head

		head = next_node


	# after sorting, join the partition
	if left_tail is None:
		return right_head
	else:
		if right_head is not None:
			left_tail.next = right_head
		return left_head
		


# test case
# expected result: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
x = 5

values = [3, 5, 8, 5, 10, 2, 1]
head = None

for value in values:
	head = add(head, value)

print('linked list adding all nodes:')
print_linked_list(head)
print()

print('linked list after partitioning:')
partitioned_head = partition(head, x)
print_linked_list(partitioned_head)

