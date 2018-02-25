"""
You are given a binary tree in which each node contains an integer value
(which might be positive or negative). Design an algorithm to count the
number of paths that sum to a given value. The path does not need to
start or end at the root or a leaf, but it must go downwards (traveling
only from parent nodes to child nodes).
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

    def __repr__(self):
        left = None
        right = None

        if self.left is not None:
            left = self.left.data
        if self.right is not None:
            right = self.right.data

        return 'data: {0}  left: {1}  right: {2}'.format(self.data, left, right)


def print_level_order(head):
    queue = [head]

    while len(queue) > 0:
        head_node = queue.pop(0)
        print(head_node)
        if head_node.left is not None:
            queue.append(head_node.left)
        if head_node.right is not None:
            queue.append(head_node.right)


def count_paths(head, target_sum, running_sum=0, paths_list={}):
    # Base case
    if head is None:
        return 0

    # Current total
    running_sum += head.data

    # Find total_paths
    total_paths = 0  # placeholder

    if running_sum == target_sum:
        total_paths += 1

    current_sum = running_sum - target_sum


    # Manage paths list
    if running_sum not in paths_list:
        paths_list[running_sum] = 1  # First path with that running sum
    else:
        paths_list[running_sum] += 1


    # Count
    total_paths += count_paths(head.left, target_sum, running_sum, paths_list)
    total_paths += count_paths(head.right, target_sum, running_sum, paths_list)

    

    return total_paths







