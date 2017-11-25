"""
Design an algorithm to write code to find the first common ancestor of two
nodes in a binary tree. Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.
"""


class Node:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


def common_ancestor(node1, node2):
    # assumes that only one of the nodes can be the root node
    if node1.parent is None:
        # print('first node\'s parent is none')
        node_ahead = node1
        node_behind = node2
    elif node2.parent is None:
        # print('second node\'s parent is none')
        node_ahead = node2
        node_behind = node1
    else:
        # print('neither of the nodes are root')
        node_ahead = node2
        node_behind = node1


    while node_ahead is not None:
        parent_1 = node_ahead

        while node_behind is not None:
            parent_2 = node_ahead

            #if (parent_1.data == parent_2.data) and (parent_1.left == parent_2.left) and (parent_1.right == parent_2.right):
            if parent_1 == parent_2:
                left = None
                if parent_2.left is not None:
                    left = parent_2.left.data

                right = None
                if parent_2.right is not None:
                    right = parent_2.right.data

                return parent_2.data, left, right

            node_behind = node_behind.parent

        node_ahead = node_ahead.parent

    return None









