# Depth-first search, pre-order travel, from the answer key.


class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class LinkedNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def append_node(self, item):
        if self.data is None:
            self.data = item
        else:
            current_node = self
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = LinkedNode(item)


def print_results(depth_lists):
    # Expects a list of linked lists.
    for first_node in depth_lists:
        current_node = first_node
        while current_node is not None:
            print(current_node, end=' ')
            current_node = current_node.next
        print()

    print()


def list_of_depths(root, depth_lists=None, level=0):
    # Runs on O(N) time.
    # Uses O(log N) recursive calls in a balanced tree, where each call adds a
    # new level to the stack, but space-wise, is dwarfed by the O(N) data
    # being returned.

    # Base case
    if root is None:
        return None

    # First time this function is called.
    if depth_lists is None:
        depth_lists = []

    # Retrieve the linked list associated with the current level,
    # or create one if there isn't one.
    if len(depth_lists) == level:
        # Level not contained in list.
        # Levels are always traversed in order. So if this is the first time we've
        # visited level i, we must have seen levels 0 through (i-1). We can
        # therefore safely add the level at the end.
        this_level = LinkedNode()
        depth_lists.append(this_level)
    else:
        # Root of the tree is depth 0.
        this_level = depth_lists[level]

    # Add the root to the current depth list.
    this_level.append_node(root)

    # Recursing the next levels.
    list_of_depths(root.left, depth_lists, level+1)
    list_of_depths(root.right, depth_lists, level+1)

    return depth_lists

