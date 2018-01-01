# Test cases for check subtree problem.


from check_subtree import *


# Tree 1: basic tree, no similarities
node_2 = Node(2)
node_12 = Node(12, node_2)
node_1 = Node(1)
node_7 = Node(7, node_1, node_12)
node_9 = Node(9)
node_5 = Node(5, node_9, node_7)
node_3 = Node(3)
node_11 = Node(11, node_3)
node_4 = Node(4, None, node_11)
tree_1_root = Node(8, node_5, node_4)

# test case 1: False
node_a = Node(5)
node_b = Node(4)
tree_2_root = Node(8, node_a, node_b)

result = check_subtree(tree_1_root, tree_2_root)
print(result)

# test case 2: True
node_a = Node(2)
node_b = Node(12, node_a)
node_c = Node(1)
tree_2_root = Node(7, node_c, node_b)

result = check_subtree(tree_1_root, tree_2_root)
print(result)

# test case 3: True
node_a = Node(3)
tree_2_root = Node(11, node_a)

result = check_subtree(tree_1_root, tree_2_root)
print(result)

# test case 4: False
tree_2_root = Node(4)

result = check_subtree(tree_1_root, tree_2_root)
print(result)

