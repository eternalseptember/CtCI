# Implementing a solution to the random node problem.


from random import *


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = 1


    def get_random_node(self):
        if self.left is None:
            left_size = 0
        else:
            left_size = self.left.size

        # Java's nextInt(n) returns a random number
        # between 0 (inclusive) and n (exclusive).
        # randint in inclusive for both boundaries.
        random_index = randint(0, self.size)



        return None

    def insert_in_order(self, item):
        if item <= self.data:
            if self.left is None:
                self.left = Node(item)
            else:
                self.left.insert_in_order(item)
        else:
            if self.right is None:
                self.right = Node(item)
            else:
                self.right.insert_in_order(item)

        self.size += 1

    def find(self, item):
        if item == self.data:
            return self
        elif item <= self.data:
            if self.left is not None:
                return self.left.find(item)
            else:
                return None
        elif item > self.data:
            if right is not None:
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

        return 'data: {0}  left: {1}  right: {2}'.format(self.data, left, right)







