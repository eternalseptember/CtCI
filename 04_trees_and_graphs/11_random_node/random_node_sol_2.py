# Option #7


from random import *


class Tree:
    def __init__(self, root=None):
        self.root = root  # should be a TreeNode.


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


    def __str__(self):
        return str(self.root)


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = 1


    def get_ith_node(self, i):
        if self.left is None:
            left_size = 0
        else:
            left_size = self.left.size

        if i < left_size:
            return self.left.get_ith_node(i)
        elif i == left_size:
            return self
        else:
            # skipping over left_size + 1 nodes, so subtract them
            return self.right.get_ith_node(i - (left_size + 1))


    def insert_in_order(self, item):
        if item <= self.data:
            if self.left is None:
                self.left = TreeNode(item)
            else:
                self.left.insert_in_order(item)
        else:
            if self.right is None:
                self.right = TreeNode(item)
            else:
                self.right.insert_in_order(item)

        self.size += 1


    def find(self, item):
        # returns a TreeNode
        if item == self.data:
            return self
        elif item <= self.data:
            if self.left is not None:
                return self.left.find(item)
            else:
                return None
        elif item > self.data:
            if self.right is not None:
                return self.right.find(item)
            else:
                return None
        return None


    def __str__(self):
        left = None
        right = None

        if self.left is not None:
            left = self.left.data
        if self.right is not None:
            right = self.right.data

        return 'data: {0}  left: {1}  right: {2}  size: {3}'.format(self.data, left, right, self.size)


def print_tree(root):
    head = root.root
    queue = [head]

    while len(queue) > 0:
        head_node = queue.pop(0)
        print(head_node)
        if head_node.left is not None:
            queue.append(head_node.left)
        if head_node.right is not None:
            queue.append(head_node.right)



