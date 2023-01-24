"""
Implement an algorithm to find the kth to last element of a singly linked list.
"""

"""
Solution presented:
k = 1 would return the last element
k = 2 would return the second-to-last element

Alternative implementation could:
k = 0 would return last element
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


"""
def find_element(k, head):
	# This probably corresponds to
	# Solution 1: If linked list size is known.

	if head is None:
		return None

	items = []

	while head.next is not None:
		items.append(head.data)
		head = head.next

	if len(items) < k:
		return None
	else:
		return items[-k]
"""


def find_element(k, head):
	"""
	Use two pointers and place them k nodes apart.
	O(N) time and O(1) space.
	"""
	if head is None:
		return None

	p1 = head
	p2 = head

	# Move p1 ahead of p2 by k steps
	for steps in range(k):
		if p1 is None:
			return None
		else:
			p1 = p1.next

	# When p1 hits the end, return p2
	while p1 is not None:
		p1 = p1.next
		p2 = p2.next

	return p2

