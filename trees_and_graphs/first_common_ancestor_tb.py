# Test cases for first common ancestor problem.

# from first_common_ancestor import *
from first_common_ancestor_sol import *


# test 1: node 8
node9 = Node(9)
node1 = Node(1)
node2 = Node(2)
node12 = Node(12, node2)
node2.parent = node12
node7 = Node(7, node1, node12)
node1.parent = node7
node12.parent = node7
node5 = Node(5, node9, node7)
node9.parent = node5
node7.parent = node5
node3 = Node(3)
node11 = Node(11, node3)
node3.parent = node11
node4 = Node(4, None, node11)
node11.parent = node4
node8 = Node(8, node5, node4)
node5.parent = node8
node4.parent = node8

ancestor = common_ancestor(node5, node4)
print(ancestor)


# test 2: node 2
node1 = Node(1)
node3 = Node(3)
node2 = Node(2, node1, node3)
node1.parent = node2
node3.parent = node2

ancestor = common_ancestor(node1, node3)
print(ancestor)


# Testing the arguments order
# test 3: node1 is higher than node2
node2 = Node(2)  # leaf
node1 = Node(1, node2)  # root
node2.parent = node1

ancestor = common_ancestor(node1, node2)
print(ancestor)


# test 4: node2 is higher than node1
node1 = Node(1)  # leaf
node2 = Node(2, node1)  # root
node1.parent = node2

ancestor = common_ancestor(node1, node2)
print(ancestor)

