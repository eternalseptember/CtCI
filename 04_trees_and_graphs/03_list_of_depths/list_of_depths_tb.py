# Test cases for "list of depths" problem


# from list_of_depths import *
# from list_of_depths_sol_1 import *
from list_of_depths_sol_2 import *


# testing; depth: 3
node8 = TreeNode(8)
node9 = TreeNode(9)
node5 = TreeNode(5, node8, node9)
node4 = TreeNode(4)
node2 = TreeNode(2, node4, node5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node3 = TreeNode(3, node6, node7)
node1 = TreeNode(1, node2, node3)

lists = list_of_depths(node1)
print_results(lists)



# testing: depth 4
node5 = TreeNode(5)
node4 = TreeNode(4, None, node5)
node3 = TreeNode(3, node4)
node2 = TreeNode(2, None, node3)
node1 = TreeNode(1, None, node2)

lists = list_of_depths(node1)
print_results(lists)



