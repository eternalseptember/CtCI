"""
Design an algorithm to write code to find the first common ancestor of two
nodes in a binary tree. Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.

Original personal attempt
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
    # Assumes that only one of the nodes can be the root node.
    if node1.parent is None:
        node_ahead = node1
        node_behind = node2
    else:
        node_ahead = node2
        node_behind = node1

    orig_node_behind = node_behind
    while node_ahead is not None:

        # reset the original node
        node_behind = orig_node_behind
        while node_behind is not None:

            if node_behind == node_ahead:
                return node_behind

            node_behind = node_behind.parent
        node_ahead = node_ahead.parent

    return None









