# Simple approach: check substring?


class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        left = None
        right = None

        if self.left is not None:
            left = self.left.data
        if self.right is not None:
            right = self.right.data

        return 'data: {0}  left: {1}  right: {2}'.format(self.data, left, right)


def pre_order(root):
    if root.data is None:
        seq = ['X']
    else:
        seq = [root.data]

    seq.extend(pre_order(root.left))
    seq.extend(pre_order(root.right))

    return seq


def check_subtree(tree_1, tree_2):
    # checks if tree_2 is a subtree of tree_1
    return False









