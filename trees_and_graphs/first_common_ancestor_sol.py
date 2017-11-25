"""
Implementing the solution for first common ancestor problem.
"""


class Node:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


def common_ancester(node1, node2):
    return None


def go_up_by(node, number):
    return None


def depth(node):
    depth = 0

    while node is not None:
        node = node.parent
        depth += 1

    return depth








