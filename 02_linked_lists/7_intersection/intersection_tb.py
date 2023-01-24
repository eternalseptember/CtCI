# Test cases for the "intersection" problem.


from intersection import *


# Test case 1: Intersecting
# Linked list setup
linked_node_a = Node(1)
linked_node_b = Node(2, linked_node_a)
linked_node_c = Node(7, linked_node_b)

linked_node_d = Node(9, linked_node_c)
linked_node_e = Node(5, linked_node_d)
linked_node_f = Node(1, linked_node_e)
linked_node_g = Node(3, linked_node_f)  # head_1

linked_node_h = Node(6, linked_node_c)
linked_node_i = Node(4, linked_node_h)  # head_2

"""
# Expected result: a node
head_1 = linked_node_g
head_2 = linked_node_i
intersection = find_intersection(head_1, head_2)

if intersection is not None:
	print_linked_list(intersection)
else:
	print('No intersection')
print()
"""

# **************************************************************

# Test case 2: Not intersecting
# List 1
list_1_a = Node(1)
list_1_b = Node(2, list_1_a)
list_1_c = Node(7, list_1_b)
list_1_d = Node(9, list_1_c)
list_1_e = Node(5, list_1_d)
list_1_f = Node(1, list_1_e)
list_1_g = Node(3, list_1_f)  # head_1


# List 2
list_2_a = Node(1)
list_2_b = Node(2, list_2_a)
list_2_c = Node(7, list_2_b)
list_2_d = Node(6, list_2_c)
list_2_e = Node(4, list_2_d)  # head_2

"""
# Expected result: no intersection
head_1 = list_1_g
head_2 = list_2_e
intersection = find_intersection(head_1, head_2)

if intersection is not None:
	print_linked_list(intersection)
else:
	print('No intersection')
print()
"""

# **************************************************************

# Testing helper functions

# Question: Are these nodes the same?
"""
if list_1_a == list_2_a:
	print('these two nodes are the same')
else:
	print('these two nodes are different')
"""

# Question: Are these nodes intersected?
# Test case 1: True
print(is_intersected(linked_node_g, linked_node_i))

# Test case 2: False
print(is_intersected(list_1_g, list_2_e))

