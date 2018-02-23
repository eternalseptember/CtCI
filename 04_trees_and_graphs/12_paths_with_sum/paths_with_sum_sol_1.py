# Solution 1: Brute Force
# In a balanced tree, runtime is O(N log N).
# In an unbalanced tree, O(N^2).


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


def count_paths(head, target_sum):
    if head is None:
        return 0

    # Count paths with sum starting from the root
    paths_from_root = count_paths_from_node(head, target_sum, 0)

    # Try the nodes on the left and right
    paths_on_left = count_paths(head.left, target_sum)
    paths_on_right = count_paths(head.right, target_sum)

    return paths_from_root + paths_on_left + paths_on_right


def count_paths_from_node(head, target_sum, current_sum):
    # Returns the number of paths wht this sum starting from this node.
    if head is None:
        return 0

    current_sum += head.data

    total_paths = 0
    if current_sum == target_sum:
        total_paths += 1

    total_paths += count_paths_from_node(head.left, target_sum, current_sum)
    total_paths += count_paths_from_node(head.right, target_sum, current_sum)

    return total_paths


