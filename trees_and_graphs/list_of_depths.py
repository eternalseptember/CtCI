"""
Given a binary tree, design an algorithm which creates a linked list of
all the nodes at each depth (e.g., if you have a tree with depth D,
you'll have D linked lists).
"""


class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        """
        left = None
        right = None

        if self.left is not None:
            left = self.left.data
        if self.right is not None:
            right = self.right.data

        return 'Tree: {0}  Left: {1}  Right: {2}'.format(self.data, left, right)
        """
        return str(self.data)


class LinkedNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def print_results(depth_lists):
    # expects a list of linked lists
    for list in depth_lists:
        current_node = list
        while current_node is not None:
            print(current_node, end=' ')
            current_node = current_node.next
        print()

    print()


# Breadth-first search, iterative, from my original approach.
def list_of_depths(head):
    # Runs on O(N) time.
    # Returns O(N) data.

    if head is None:
        return None

    depth_lists = {}
    queue = [(head, 0)]

    while len(queue) > 0:
        item = queue.pop(0)
        current_node, depth = (item)

        if depth not in depth_lists:
            depth_lists[depth] = [current_node.data]
        else:
            depth_lists[depth].append(current_node.data)

        if current_node.left is not None:
            queue.append((current_node.left, depth+1))
        if current_node.right is not None:
            queue.append((current_node.right, depth+1))

    """
    # check answer here
    print('list of depths:')
    for key in depth_lists:
        print(depth_lists[key])
    """

    # convert results to linked lists
    linked_lists = []
    for key in depth_lists:
        nodes_list = depth_lists[key]

        first_node = LinkedNode(nodes_list.pop(0))
        current_node = first_node

        while len(nodes_list) > 0:
            current_node.next = LinkedNode(nodes_list.pop(0))
            current_node = current_node.next

        linked_lists.append(first_node)

    return linked_lists


# Depth-first search, pre-order travel, from the answer key.
def create_level_linked_list(root, depth_lists=None, level=0):
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
    if this_level.data is None:
        this_level.data = root
    else:
        # Travel to the end of the linked list in order to add the node.
        current_node = this_level
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = LinkedNode(root)

    # Recursing the next levels.
    create_level_linked_list(root.left, depth_lists, level+1)
    create_level_linked_list(root.right, depth_lists, level+1)

    return depth_lists




# testing; depth: 3
node8 = TreeNode(8)
node9 = TreeNode(9)
node5 = TreeNode(5, node8, node9)
node4 = TreeNode(4)
node2 = TreeNode(2, node4, node5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node3 = TreeNode(3, node6, node7)
node1 = TreeNode(1, node2, node3)

lists = list_of_depths(node1)
# lists = create_level_linked_list(node1)
print_results(lists)



# testing: depth 4
node5 = TreeNode(5)
node4 = TreeNode(4, None, node5)
node3 = TreeNode(3, node4)
node2 = TreeNode(2, None, node3)
node1 = TreeNode(1, None, node2)

lists = list_of_depths(node1)
# lists = create_level_linked_list(node1)
print_results(lists)


