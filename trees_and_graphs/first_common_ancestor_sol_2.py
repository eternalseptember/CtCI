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


def common_ancestor(root, p, q):
    # Check if either node is not in the tree, or if one covers the other.
    if (not covers(root, p)) or (not covers(root, q)):
        return None
    elif covers(p, q):
        return p
    elif covers(q, p):
        return q

    # Traverse upward until you find a node that covers q.
    sibling = get_sibling(p)
    parent = p.parent

    while (not covers(sibling, q)):
        sibling = get_sibling(parent)
        parent = parent.parent

    return parent


def covers(root, p):
    if root is None:
        return None
    if root == p:
        return True

    return covers(root.left, p) or covers(root.right, p)


def get_sibling(node):
    if (node is None) or (node.parent is None):
        return None

    parent = node.parent

    if parent.left == node:
        return parent.right
    else:
        return parent.left






