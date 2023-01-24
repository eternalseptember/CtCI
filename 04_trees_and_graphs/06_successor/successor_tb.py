# Test cases for "successor" problem.


# from successor import *
from successor_sol import *


"""
# ************************************************
# ******************** TREE 1 ********************
# ************************************************

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

# in-order: 1, 3, 4, 6, 7, 8, 10, 13, 14
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

# in-order: 1 2 3 4 5
list_of_nodes = [node1, node2, node3, node4, node5]
for single_node in list_of_nodes:
	next_node = find_next_node(single_node)
	print(next_node)
print()
"""

# ************************************************
# ******************** TREE 3 ********************
# ************************************************

node3 = Node(3)
node4 = Node(4, node3)
node3.prev = node4
node2 = Node(2, None, node4)
node4.prev = node2
node1 = Node(1, None, node2)
node2.prev = node1

#print_tree(node1)

# in-order: 1 2 3 4
list_of_nodes = [node1, node2, node3, node4]
for single_node in list_of_nodes:
	next_node = find_next_node(single_node)
	print(next_node)
print()

"""
# ************************************************
# ******************** TREE 4 ********************
# ************************************************

node7 = Node(7)
node8 = Node(8, node7)
node7.prev = node8
node10 = Node(10)
node9 = Node(9, node8, node10)
node8.prev = node9
node10.prev = node9

node4 = Node(4)
node5 = Node(5, node4)
node4.prev = node5
node6 = Node(6, node5 ,node9)
node5.prev = node6
node9.prev = node6

node3 = Node(3, None, node6)
node6.prev = node3

node1 = Node(1)
node2 = Node(2, node1, node3)
node1.prev = node2
node3.prev = node2

#print_tree(node2)

# in-order: 1 2 3 4 5 6 7 8 9 10
list_of_nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10]
for single_node in list_of_nodes:
	next_node = find_next_node(single_node)
	print(next_node)
print()


# ************************************************
# ******************** TREE 5 ********************
# ************************************************

node3 = Node(3)
node4 = Node(4, node3)
node3.prev = node4
node5 = Node(5, node4)
node4.prev = node5
node6 = Node(6, node5)
node5.prev = node6
node7 = Node(7, node6)
node6.prev = node7
node2 = Node(2, None, node7)
node7.prev = node2
node1 = Node(1, None, node2)
node2.prev = node1

#print_tree(node1)

# in-order: 1 2 3 4 5 6 7
list_of_nodes = [node1, node2, node3, node4, node5, node6, node7]
for single_node in list_of_nodes:
	next_node = find_next_node(single_node)
	print(next_node)
print()


# ************************************************
# ******************** TREE 6 ********************
# ************************************************

node3 = Node(3)
node5 = Node(5)
node4 = Node(4, node3, node5)
node3.prev = node4
node5.prev = node4
node6 = Node(6, node4)
node4.prev = node6
node1 = Node(1)
node2 = Node(2, node1, node6)
node1.prev = node2
node6.prev = node2
node7 = Node(7, node2)
node2.prev = node7

node12 = Node(12)
node11 = Node(11, None, node12)
node12.prev = node11
node9 = Node(9)
node10 = Node(10, node9, node11)
node9.prev = node10
node11.prev = node10

node8 = Node(8, node7, node10)
node7.prev = node8
node10.prev = node8

#print_tree(node8)

# in-order: 1 2 3 4 5 6 7 8 9 10 11 12
list_of_nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12]
for single_node in list_of_nodes:
	next_node = find_next_node(single_node)
	print(next_node)
print()
"""

# ************************************************
# ******************** TREE 7 ********************
# ************************************************

node3 = Node(3)
node4 = Node(4, node3)
node3.prev = node4
node2 = Node(2, None, node4)
node4.prev = node2
node1 = Node(1, None, node2)
node2.prev = node1
node6 = Node(6)
node5 = Node(5, node1, node6)
node1.prev = node5
node6.prev = node5
node7 = Node(7, node5)
node5.prev = node7

#print_tree(node7)

# in-order: 1 2 3 4 5 6 7
list_of_nodes = [node1, node2, node3, node4, node5, node6, node7]
for single_node in list_of_nodes:
	next_node = find_next_node(single_node)
	print(next_node)
print()

