# Solution 2: Optimized


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


def count_paths(head, target_sum, running_sum=0, path_count={}):
    # Base case
    if head is None:
        return 0

    # Count paths with sum ending at the current node.
    running_sum += head.data
    current_sum = running_sum - target_sum
    # total_paths = path_count.get_or_default(current_sum, 0)
    if current_sum not in path_count:
        total_paths = 0
    else:
        total_paths = path_count[current_sum]

    # If running_sum equals target_sum, then one additional path starts at root.
    # Add in this path.
    if running_sum == target_sum:
        total_paths += 1

    # Increment path_count, recurse, then decrement path_count
    increment_hash_table(path_count, running_sum, 1)  # Increment path_count
    total_paths += count_paths(head.left, target_sum, running_sum, path_count)
    total_paths += count_paths(head.right, target_sum, running_sum, path_count)
    increment_hash_table(path_count, running_sum, -1)  # Decrement path_count

    return total_paths


def increment_hash_table(hash_table, key, delta):
    # new_count = hash_table.get_or_default(key, 0) + delta
    if key not in hash_table:
        new_count = delta
    else:
        new_count = hash_table[key] + delta


    if new_count == 0:
        # remove when zero to reduce space usage
        hash_table.pop(key)
    else:
        hash_table[key] = new_count




