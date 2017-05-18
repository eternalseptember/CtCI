"""
You are implementing a binary tree class from scratch which, in addition to
insert, find, and delete, has a method getRandomNode() which returns a random
node from the tree. All nodes should be equally likely to be chosen. Design
and implement an algorithm for getRandomNode, and explain how you would
implement the rest of the methods.
"""


class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def __str__(self):
		left = None
		right = None

		if self.left is not None:
			left = self.left.data
		if self.right is not None:
			right = self.right.data

		return 'data: {0}  left: {1}  right: {2}'.format(self.data, left, right)


def print_level_order(head):
	queue = [head]

	while len(queue) > 0:
		head_node = queue.pop(0)
		print(head_node)
		if head_node.left is not None:
			queue.append(head_node.left)
		if head_node.right is not None:
			queue.append(head_node.right)


def insert(head, data):
	if head is None:
		return Node(data)

	queue = [head]

	while len(queue) > 0:
		single_node = queue.pop(0)

		if single_node.left is not None:
			queue.append(single_node.left)
		else:
			single_node.left = Node(data)
			return head

		if single_node.right is not None:
			queue.append(single_node.right)
		else:
			single_node.right = Node(data)
			return head



def find(head, target):
	# find a node based on values
	queue = [head]

	while len(queue) > 0:
		current_node = queue.pop(0)

		left_match = False
		right_match = False

		if (current_node.left is None) and (target.left is None):
			left_match = True
		elif (current_node.left is not None) and (target.left is not None):
			if (current_node.left.data == target.left.data):
				left_match = True

		if (current_node.right is None) and (target.right is None):
			right_match = True
		elif (current_node.right is not None) and (target.right is not None):
			if (current_node.right.data == target.right.data):
				right_match = True


		if (current_node.data == target.data) and (left_match is True) and (right_match is True):
			return True
		else:
			if current_node.left is not None:
				queue.append(current_node.left)
			if current_node.right is not None:
				queue.append(current_node.right)

	return False


def delete(head, target):
	# remove the first node with matching head data, left data, and right data
	# return True if node has been deleted
	# return False if node cannot be deleted
	queue = [head]

	while len(queue) > 0:
		current_node = queue.pop(0)

		left_match = False
		right_match = False

		if (current_node.left is None) and (target.left is None):
			left_match = True
		elif (current_node.left is not None) and (target.left is not None):
			if (current_node.left.data == target.left.data):
				left_match = True

		if (current_node.right is None) and (target.right is None):
			right_match = True
		elif (current_node.right is not None) and (target.right is not None):
			if (current_node.right.data == target.right.data):
				right_match = True


		if (current_node.data == target.data) and (left_match is True) and (right_match is True):
			# remove node here



			return True
		else:
			if current_node.left is not None:
				queue.append(current_node.left)
			if current_node.right is not None:
				queue.append(current_node.right)

	return False


def get_random_node(head):
	# return ranodm node
	return None


# testing
values = [7, 5, 3, 8, 1, 8, 0, 2, 5, 2, 4, 1]
# values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
head = None

for value in values:
	head = insert(head, value)

print_level_order(head)

"""
# test case 1: true
node2 = Node(2)
node4 = Node(4)
look_for_this_node = Node(1, node2, node4)

found_node = find(head, look_for_this_node)
print(found_node)


# test case 2: true
look_for_this_node = Node(2)

found_node = find(head, look_for_this_node)
print(found_node)


# test case 3: false
look_for_this_node = Node(7)

found_node = find(head, look_for_this_node)
print(found_node)


# test case 4: false
node0 = Node(0)
node4 = Node(4)
look_for_this_node = Node(1, node0, node4)

found_node = find(head, look_for_this_node)
print(found_node)


# test case 5: false
node4 = Node(4)
look_for_this_node = Node(1, None, node4)

found_node = find(head, look_for_this_node)
print(found_node)


# test case 6: true
node1 = Node(1)
look_for_this_node = Node(8, node1)

found_node = find(head, look_for_this_node)
print(found_node)
"""


# test 1 delete: true
target_node = Node(1)

delete_success = delete(head, target_node)
print(delete_success)


# test 2 delete: false
node5 = Node(5)
node2 = Node(2)
target_node = Node(7, node5, node2)

delete_success = delete(head, target_node)
print(delete_success)





