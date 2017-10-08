"""
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.
"""


class Node:
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


def print_tree(head):
    queue = [head]

    while len(queue) > 0:
        head_node = queue.pop(0)
        print(head_node)
        if head_node.left is not None:
            queue.append(head_node.left)
        if head_node.right is not None:
            queue.append(head_node.right)


def create_minimal_tree(list_of_values):
    len_of_list = len(list_of_values)

    # base case
    if len_of_list == 0:
        return None

    # divide the tree into three parts
    center_index = len_of_list // 2
    left_list = list_of_values[:center_index]
    right_list = list_of_values[center_index+1:]

    left_tree = create_minimal_tree(left_list)
    right_tree = create_minimal_tree(right_list)

    head = Node(list_of_values.pop(center_index), left_tree, right_tree)
    return head


# Test case 1: odd number of elements
# root of the tree: 5, left: 2, right: 8
list_of_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

head = create_minimal_tree(list_of_values)
print('Odd number of elements')
print_tree(head)
print()


# Test case 2: even number of elements
list_of_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

head = create_minimal_tree(list_of_values)
print('Even number of elements')
print_tree(head)
print()






