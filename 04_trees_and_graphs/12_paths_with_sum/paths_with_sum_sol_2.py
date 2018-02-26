# Solution 2: Optimized
# O(N) time, where N is the number of nodes in the tree,
# because it travels to each ndoe once, doing O(1) work each time.
# In a balanced tree, the space is O(log N) due to the hash table.
# In an unbalanced tree, space can grow to O(N).


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


def count_paths(head, target_sum, running_sum=0, paths_counts={}):
    # Base case
    if head is None:
        return 0

    # Count paths with sum ending at the current node.
    running_sum += head.data
    current_sum = running_sum - target_sum
    # total_paths = paths_counts.get_or_default(current_sum, 0)
    if current_sum not in paths_counts:
        total_paths = 0
    else:
        total_paths = paths_counts[current_sum]

    # If running_sum equals target_sum, then one additional path starts at root.
    # Add in this path.
    if running_sum == target_sum:
        total_paths += 1

    # Increment paths_counts, recurse, then decrement paths_counts
    increment_paths_counts(paths_counts, running_sum, 1)  # Increment
    total_paths += count_paths(head.left, target_sum, running_sum, paths_counts)
    total_paths += count_paths(head.right, target_sum, running_sum, paths_counts)
    increment_paths_counts(paths_counts, running_sum, -1)  # Decrement

    return total_paths


def increment_paths_counts(paths_counts, running_sum, count):
    # new_count = paths_counts.get_or_default(running_sum, 0) + count
    if running_sum not in paths_counts:
        new_count = count
    else:
        new_count = paths_counts[running_sum] + count


    if new_count == 0:
        # remove when zero to reduce space usage
        paths_counts.pop(running_sum)
    else:
        paths_counts[running_sum] = new_count




