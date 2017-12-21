# Implementing the provided solution.


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def bst_sequences(head):
    result = []

    if head is None:
        return result



