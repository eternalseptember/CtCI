"""
Implementing the solution for first common ancestor problem.

Solution 2: With links to parent (better worst-case runtime)
"""


class Node:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        data = self.data
        left = None
        right = None

        if self.left is not None:
            left = self.left.data
        if self.right is not None:
            right = self.right.data

        return 'node: {0}  left: {1}  right: {2}'.format(data, left, right)


def common_ancestor(node1, node2):
    return None


def covers(root, p):
    if root is None:
        return None
    if root == p:
        return True
    # another return statement here


def get_sibling(node):
    if (node is None) or (node.parent is None):
        return None

    parent = node.parent

    # return a comparison






