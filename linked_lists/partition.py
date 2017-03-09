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
	return None


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

partitioned_head = partition(head, x)


