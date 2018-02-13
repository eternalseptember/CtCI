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
        return None

    # Count paths with sum ending at the current node.
    running_sum += head.data
    current_sum = running_sum - target_sum
    # total_paths = path_count.get_or_default(current_sum, 0)


def increment_hash_table(hash_table, key, delta):
    # new_count = hash_table.get_or_default(key, 0) + delta
    new_count = 0  # placefiller line
    if new_count == 0:
        # remove when zero to reduce space usage
        hash_table.remove(key)
    else:
        hash_table.put(key, new_count)




