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


"""
Original attempt was brute force:
First, it enumerated all of the paths in the tree and stored those paths
in a list. Time: O(N log N), where N is the number of nodes.

Then, my algorithm went through each path in the list and totalled the
value of the nodes. The total_paths was incremented if and only if the
total was equal to the target sum, and the path was unique.


Errors in reasoning:
1.) The problem said that the path does not need to start at the root
    or end at the the leaf. My original attempt did not account for this,
    which resulted in wrong expected answers in my test cases.
2.) I only counted paths that were unique. The original purpose was to
    not count the same path fragment multiple times (in the event that I
    correctly accounted for the caveat in the previous point), but it does
    not account for the valid possibility that some values/paths could be
    duplicated in the tree.
3.) And therefore, I didn't have to store the list of paths. I only had to
    store the number of paths for each sum.
4.) In the optimized solution, the decrement hash table does what my
    original get_paths function did by backtracking the counts.
"""


def count_paths(head, target_sum, running_sum=0, paths_counts={}):
    # Base case
    if head is None:
        return 0


    # The sum ends at the current node.
    # running_sum begins at the root.
    # current_sum 
    running_sum += head.data
    current_sum = running_sum - target_sum


    # 
    if current_sum not in paths_counts:
        total_paths = 0
    else:
        total_paths = paths_counts[current_sum]

    # 
    if running_sum == target_sum:
        total_paths += 1


    # Increment paths list
    if running_sum not in paths_counts:
        paths_counts[running_sum] = 1  # First path with that running sum
    else:
        paths_counts[running_sum] += 1


    # Count
    total_paths += count_paths(head.left, target_sum, running_sum, paths_counts)
    total_paths += count_paths(head.right, target_sum, running_sum, paths_counts)


    # Decrement paths list
    if (paths_counts[running_sum] - 1) == 0:
        paths_counts.pop(running_sum)
    else:
        paths_counts[running_sum] -= 1


    return total_paths







