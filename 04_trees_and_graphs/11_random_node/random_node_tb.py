# Test cases for random node problem.


from random_node import *


# testing
values = [7, 5, 3, 8, 1, 8, 0, 2, 5, 2, 4, 1]
# values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
head = None

for value in values:
	head = insert(head, value)

print('original tree')
print_level_order(head)
print()


"""
# test case 1: true
node2 = Node(2)
node4 = Node(4)
look_for_this_node = Node(1, node2, node4)

found_status, found_node, parent_node = find(head, look_for_this_node)
print(found_status)


# test case 2: true
look_for_this_node = Node(2)

found_status, found_node, parent_node = find(head, look_for_this_node)
print(found_status)


# test case 3: false
look_for_this_node = Node(7)

found_status, found_node, parent_node = find(head, look_for_this_node)
print(found_status)


# test case 4: false
node0 = Node(0)
node4 = Node(4)
look_for_this_node = Node(1, node0, node4)

found_status, found_node, parent_node = find(head, look_for_this_node)
print(found_status)


# test case 5: false
node4 = Node(4)
look_for_this_node = Node(1, None, node4)

found_status, found_node, parent_node = find(head, look_for_this_node)
print(found_status)


# test case 6: true
node1 = Node(1)
look_for_this_node = Node(8, node1)

found_status, found_node, parent_node = find(head, look_for_this_node)
print(found_status)
"""


# test 1 random node:
for i in range(15):
	random_node = get_random_node(head)
	print(random_node)
	print()


