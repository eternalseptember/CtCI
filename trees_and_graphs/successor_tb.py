"""
test cases for successor problem
"""


from successor import *

# ************************************************
# ******************** TREE 1 ********************
# ************************************************

# in-order: 1, 3, 4, 6, 7, 8, 10, 13, 14
node13 = Node(13)
node14 = Node(14, node13)
node13.prev = node14
node10 = Node(10, None, node14)
node14.prev = node10

node4 = Node(4)
node7 = Node(7)
node6 = Node(6, node4, node7)
node4.prev = node6
node7.prev = node6

node1 = Node(1)
node3 = Node(3, node1, node6)
node1.prev = node3
node6.prev = node3

node8 = Node(8, node3, node10)
node3.prev = node8
node10.prev = node8

#print_tree(node8)

print('tree 1')
left_half = [node1, node3, node4, node6, node7]
for single_node in left_half:
	next_node = find_next_node(single_node)
	print(next_node)

right_half = [node8, node10, node13, node14]
for single_node in right_half:
	next_node = find_next_node(single_node)
	print(next_node)
print()


# ************************************************
# ******************** TREE 2 ********************
# ************************************************

# in-order: 1, 2, 3, 4, 5
node3 = Node(3)
node2 = Node(2, None, node3)
node3.prev = node2
node1 = Node(1, None, node2)
node2.prev = node1

node5 = Node(5)
node4 = Node(4, node1, node5)
node1.prev = node4
node5.prev = node4

#print_tree(node4)

print('tree 2')
list_of_nodes = [node1, node2, node3, node4, node5]
for single_node in list_of_nodes:
	next_node = find_next_node(single_node)
	print(next_node)
print()


# ************************************************
# ******************** TREE 3 ********************
# ************************************************

# in-order: 1, 2, 3, 4
node3 = Node(3)
node4 = Node(4, node3)
node3.prev = node4
node2 = Node(2, None, node4)
node4.prev = node2
node1 = Node(1, None, node2)
node2.prev = node1

#print_tree(node1)

print('tree 3')
list_of_nodes = [node1, node2, node3, node4]
for single_node in list_of_nodes:
	next_node = find_next_node(single_node)
	print(next_node)
print()







