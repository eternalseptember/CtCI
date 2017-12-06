"""
Implementing the solution for first common ancestor problem.

Solution 3: Without links to parents.
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


def common_ancester(root, p, q):
    return None


def ancester_helper(root, p, q):
    if (root is None) or (root == p) or (root == q):
        return root

    return None


def covers(root, p):
    if root is None:
        return None
    if root == p:
        return True

    return covers(root.left, p) or covers(root.right, p)




