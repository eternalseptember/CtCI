# Option #7


from random import *


class Tree:
    def __init__(self, root):
        self.root = root

    # size

    def get_random_node(self):
        if self.root is None:
            return None

        # more stuff here

    def insert_in_order(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.root.insert_in_order(value)


class TreeNode:
    def __init__(self, value):
        self.value = value






