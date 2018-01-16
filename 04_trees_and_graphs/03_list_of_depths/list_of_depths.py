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

