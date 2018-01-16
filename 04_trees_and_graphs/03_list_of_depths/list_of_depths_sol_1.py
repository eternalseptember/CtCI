# Breadth-first search, iterative, from the answer key.


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


def list_of_depths(root):
    # Runs on O(N) time.
    # Returns O(N) data.
    results_list = []

    # "Visits" the root.
    current_level = LinkedNode()
    if root is not None:
        current_level.append_node(root)

    # Visits the rest of the tree.
    while current_level.data is not None:
        results_list.append(current_level)  # Add previous level
        parents = current_level  # Go to next level
        current_level = LinkedNode()

        while parents is not None:
            this_node = parents.data

            if this_node.left is not None:
                current_level.append_node(this_node.left)
            if this_node.right is not None:
                current_level.append_node(this_node.right)

            parents = parents.next

    return results_list

