# Option #7


from random import *


class Tree:
    def __init__(self, root):
        self.root = root  # should be a TreeNode


    def get_size(self):
        if self.root is None:
            return 0
        else:
            return self.root.size


    def get_random_node(self):
        if self.root is None:
            return None

        random_index = randint(0, self.root.size-1)
        return self.root.get_ith_node(random_index)


    def insert_in_order(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.root.insert_in_order(value)


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.size = 1

    def get_ith_node(self, i):
        if self.left is None:
            left_size = 0
        else:
            self.left.size()

        # skipping over left_size + 1 nodes, so subtract them

    def insert_in_order(self, item):
        return None

    def find(self, item):
        # return TreeNode
        return None





