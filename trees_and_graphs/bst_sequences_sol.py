# Implementing the provided solution.


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def add_first(self, item):
        return None

    def add_last(self, item):
        return None

    def remove_first(self):
        return None

    def remove_last(self):
        return None


def bst_sequences(head):
    result = []

    if head is None:
        # add something to the result before returning
        return result

    prefix = [head.data]

    # Recurse on left and right subtrees.
    left_seq = bst_sequences(head.left)
    right_seq = bst_sequences(head.right)

    # Weave together each list from the left and right sides.
    for left_item in left_seq:
        for right_item in right_seq:
            weaved = []
            weave_lists(left_item, right_item, weaved, prefix)
            result.extend(weaved)

    return result


def weave_lists(first_list, second_list, results, prefix):
    # Weaves lists together in all possible ways. This algorithm works by
    # removing the head from one list, recursing, and then doing the same
    # thing with the other list.

    # One list is empty. Add remainder to a cloned prefix and store result.
    if (len(first_list) == 0) or (len(second_list) == 0):
        result = []
        result.extend(first_list)
        result.extend(second_list)
        results.append(result)
        return

    # Recurse with head of first added to the prefix. Removing the head will
    # damage first, so we'll need to put it back where we found it afterwards.
    head_first = first_list.remove_first()
    prefix.add_last(head_first)
    weave_lists(first_list, second_list, results, prefix)
    prefix.remove_last()
    first_list.add_first(head_first)


    # Do the same thing with second, damaging and then restoring the list.



