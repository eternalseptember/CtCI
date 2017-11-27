"""
Implementing the solution for first common ancestor problem.

Solution 1: With links to parents
"""


class Node:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


def common_ancester(node1, node2):
    delta = depth(node1) - depth(node2)

    if delta > 0:
        first_node = node2
    else:
        first_node = node1

    return None


def go_up_by(node, delta):
    while (node is not None) and (delta > 0):
        node = node.parent
        delta -= 1
    return node


def depth(node):
    depth = 0

    while node is not None:
        node = node.parent
        depth += 1

    return depth








