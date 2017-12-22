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


def weave_lists(first_list, second_list, results, prefix):
    if (len(first_list) == 0) or (len(second_list) == 0):
        # result = clone the prefix list?
        result = []
        result.extend(first_list)
        result.extend(second_list)
        results.append(result)

