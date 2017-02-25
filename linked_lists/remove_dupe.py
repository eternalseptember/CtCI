"""
Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?
"""


class Node:
	def __init__(self, data=None, prev=None, next_node=None):
		self.data = data
		self.prev = prev
		self.next = next_node


def remove(head):
	# remove head.next
	if head is None:
		return None
	if head.next is None:
		return head

	next_node = head.next



# Setup for testing
node_a = Node(1)


