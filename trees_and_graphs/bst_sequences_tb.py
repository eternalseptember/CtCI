# Test cases for bst_sequences problem


from bst_sequences import *


# Test Case 1: {2, 1, 3}, {2, 3, 1}
node1 = Node(1)
node3 = Node(3)
node2 = Node(2, node1, node3)

results = bst_sequences(node2)
print(results)


# Test Case 2 (left node): {2, 1}
node1 = Node(1)
node2 = Node(2, node1)

results = bst_sequences(node2)
print(results)


# Test Case 3 (right node): {2, 1}
node1 = Node(1)
node2 = Node(2, None, node1)

results = bst_sequences(node2)
print(results)


# Test Case 4: [{2, 1, 4, 3}, {2, 3, 1, 4}] ??
node4 = Node(4)
node1 = Node(1, node4)
node3 = Node(3)
node2 = Node(2, node1, node3)

results = bst_sequences(node2)
print(results)


# Test Case 5:
node1 = Node(1)
node3 = Node(3)
node2 = Node(2, node1, node3)
node6 = Node(6)
node5 = Node(5, None, node6)
node4 = Node(4, node2, node5)

results = bst_sequences(node4)
print(results)
print()


# Test Case 6: From the example in the solution
node5 = Node(5)
node15 = Node(15)
node10 = Node(10, node5, node15)
node25 = Node(25)
node20 = Node(20, node10, node25)

node65 = Node(65)
node80 = Node(80)
node70 = Node(70, node65, node80)
node60 = Node(60, None, node70)

node50 = Node(50, node20, node60)

results = bst_sequences(node50)
print(results)






