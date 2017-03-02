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




