# Test cases for the "check balanced" problem.


# from check_balanced import *
from check_balanced_sol import *


# Test Case 1: True; height_diff = 0
node1 = Node(1)
node2 = Node(2)
node3 = Node(3, node1, node2)
print(is_binary(node3))


# Test Case 2: True; height_diff = 1
node1 = Node(1)
node2 = Node(2, node1)
print(is_binary(node2))


# Test Case 3: True; height_diff = -1
node1 = Node(1)
node2 = Node(2, None, node1)
print(is_binary(node2))


# Test Case 4: False; height_diff = -5
node6 = Node(6)
node5 = Node(5, None, node6)
node4 = Node(4, None, node5)
node3 = Node(3, None, node4)
node2 = Node(2, None, node3)
node1 = Node(1, None, node2)
print(is_binary(node1))


# Test Case 5: False; height_diff = -2
node1 = Node(1)
node2 = Node(2, None, node1)
node3 = Node(3)
node4 = Node(4, node3, node2)
node5 = Node(5)
node6 = Node(6, node5, node4)
print(is_binary(node6))


# Test Case 6: True; height_diff = -1
node1 = Node(1)
node3 = Node(3)
node2 = Node(2, node1, node3)
node8 = Node(8)
node7 = Node(7, None, node8)
node5 = Node(5)
node6 = Node(6, node5, node7)
node4 = Node(4, node2, node6)
print(is_binary(node4))


# Test Case 7: False; height_diff = -2
node1 = Node(1)
node2 = Node(2, node1)
node3 = Node(3, None, node2)
print(is_binary(node3))



