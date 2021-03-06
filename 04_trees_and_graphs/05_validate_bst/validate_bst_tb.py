# Test cases for the "validate bst" problem.


# from validate_bst import *
from validate_bst_sol import *


# Simple test cases to handle duplicate values
# Test case A: True
node1 = Node(20)
node2 = Node(20, node1)

print(check_bst(node2))


# Test case B: False
node1 = Node(20)
node2 = Node(20, None, node1)

print(check_bst(node2))


# Definition: ALL left nodes must be less than or equal to current node,
# which must be less than all the right nodes.
# Test case 1: False
node1 = Node(25)
node2 = Node(10, None, node1)
node3 = Node(30)
node4 = Node(20, node2, node3)

print(check_bst(node4))


print()
# Complex trees
# Test case 1: True
node1 = Node(1)
node4 = Node(4)
node7 = Node(7)
node6 = Node(6, node4, node7)
node3 = Node(3, node1, node6)
node13 = Node(13)
node14 = Node(14, node13)
node10 = Node(10, None, node14)
node8 = Node(8, node3, node10)

print(check_bst(node8))


# Test case 2: False
node2 = Node(2)
node1 = Node(1)
node9 = Node(9)
node12 = Node(12, node2)
node7 = Node(7, node1, node12)
node5 = Node(5, node9, node7)
node3 = Node(3)
node11 = Node(11, node3)
node4 = Node(4, None, node11)
node8 = Node(8, node5, node4)

print(check_bst(node8))


# Test case 3: True
node3 = Node(3)
node7 = Node(7)
node5 = Node(5, node3, node7)
node17 = Node(17)
node15 = Node(15, None, node17)
node10 = Node(10, node5, node15)
node30 = Node(30)
node20 = Node(20, node10, node30)

print(check_bst(node20))

