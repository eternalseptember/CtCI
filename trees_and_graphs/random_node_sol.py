class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = 1


    def get_random_node(self):
        return None


    def __str__(self):
        left = None
        right = None

        if self.left is not None:
            left = self.left.data
        if self.right is not None:
            right = self.right.data

        return 'data: {0}  left: {1}  right: {2}'.format(self.data, left, right)







