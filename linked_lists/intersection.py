"""
Given two (singly) linked lists, determine if the two lists intersect.
Return the intersecting node. Note that the intersection is defined
based on reference, not value. That is, if the kth node of the first
linked list is the exact same node (by reference) as the jth node of
the second linked list, then they are intersecting.
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


def find_intersection(head1, head2):
	# assumes that there is an intersection
	orig_head2 = head2

	while head1 is not None:
		while head2 is not None:
			if (head1.data == head2.data) and (head1.next.data == head2.next.data):
				return head2
			head2 = head2.next
		head1 = head1.next
		head2 = orig_head2

	print('no intersection found')


# testing
list1 = [3, 4, 5]
list2 = [0, 1, 2, 3, 4, 5]

head1 = None
head2 = None

for value in list1:
	head1 = add(head1, value)

for value in list2:
	head2 = add(head2, value)


print('linked list 1: ', end=' ')
print_linked_list(head1)
print()
print('linked list 2: ', end=' ')
print_linked_list(head2)
print()


print('intersection: ', end=' ')
intersection = find_intersection(head1, head2)
print_linked_list(intersection)
print()

