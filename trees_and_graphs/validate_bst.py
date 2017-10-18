"""
Implement a function to check if a binary tree is a binary search tree.
"""


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def check_bst(head):
    if head.left is not None:
        if head.left.data > head.data:
            return False
        else:
            check_bst(head.left)

    if head.right is not None:
        if head.data >= head.right.data:
            return False
        else:
            check_bst(head.right)
    return True


# Simple test cases to handle duplicate values
# Test case A: True
node1 = Node(20)
node2 = Node(20, node1)

print(check_bst(node2))


# Test case B: False
node1 = Node(20)
node2 = Node(20, None, node1)

print(check_bst(node2))


# More simple test cases
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


