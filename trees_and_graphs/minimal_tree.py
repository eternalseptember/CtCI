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

    if len_of_list == 1:
        return Node(list_of_values.pop())
    elif len_of_list == 2:
        smaller_node = Node(list_of_values.pop(0))
        return Node(list_of_values.pop(), smaller_node)
    elif len_of_list == 3:
        bigger_node = Node(list_of_values.pop())
        smaller_node = Node(list_of_values.pop(0))
        return Node(list_of_values.pop(), smaller_node, bigger_node)
    else:
        # divide the tree into three parts
        center_index = len_of_list // 2
        left_list = list_of_values[:center_index]
        right_list = list_of_values[center_index+1:]

        left_tree = create_minimal_tree(left_list)
        right_tree = create_minimal_tree(right_list)

        head = Node(list_of_values.pop(center_index), left_tree, right_tree)
        return head


# testing
list_of_values = [0]

for i in range(1, 11):
    list_of_values.append(i)
    list_of_values_copy = list_of_values[:]

    head = create_minimal_tree(list_of_values_copy)
    print_tree(head)
    print()








