"""
Implementing the solution for first common ancestor problem.

Solution 4: Optimized
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


class Result:
    def __init__(self, node, is_ancestor):
        self.node = node
        self.is_ancestor = is_ancestor


def common_ancestor(root, p, q):
    r = common_ancestor_helper(root, p, q)

    if r.is_ancestor:
        return r.node
    return None


def common_ancestor_helper(root, p, q):
    if root is None:
        return Result(None, False)

    if (root == p) and (root == q):
        return Result(root, True)

    rx = common_ancestor_helper(root.left, p, q)
    if rx.is_ancestor:
        # found common ancestor
        return rx

    ry = common_ancestor_helper(root.right, p, q)
    if ry.is_ancestor:
        # found common ancestor
        return ry

    if (rx.node is not None) and (ry.node is not None):
        return Result(root, True)  # This is the common ancestor
    elif (root == p) or (root == q):
        # if we're currently at p or q, and we also found one of those nodes
        # in a subtree, then this is truly an ancestor and the flag should be
        # true
        if (rx.node is not None) or (ry.node is not None):
            is_ancestor = True
        else:
            is_ancestor = False

        return Result(root, is_ancestor)
    else:
        if rx.node is not None:
            res = rx.node
        else:
            res = ry.node
        return Result(res, False)










"""
def common_ancestor(root, p, q):
    if root is None:
        return None

    if (root == p) and (root == q):
        return root

    x = common_ancestor(root.left, p, q)
    if (x is not None) and (x is not p) and (x is not q):
        # already found ancester
        return x

    y = common_ancestor(root.right, p, q)
    if (y is not None) and (y is not p) and (y is not q):
        # already found ancester
        return y

    if (x is not None) and (y is not None):
        # p and q found in different subtrees
        return root
    elif (root is p) or (root is q):
        return root
    else:
        # return the non-None value
        if x is None:
            return y
        else:
            return x
"""





