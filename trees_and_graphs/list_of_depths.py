"""
Given a binary tree, design an algorithm which creates a linked list of
all the nodes at each depth (e.g., if you have a tree with depth D,
you'll have D linked lists).
"""


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class LinkedNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def list_of_depths(head):
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


# Implementing solution in the answer key
def createLevelLinkedList(root, level):
    if root is None:
        return None










# testing; depth: 3
node8 = Node(8)
node9 = Node(9)
node5 = Node(5, node8, node9)
node4 = Node(4)
node2 = Node(2, node4, node5)
node6 = Node(6)
node7 = Node(7)
node3 = Node(3, node6, node7)
node1 = Node(1, node2, node3)

lists = list_of_depths(node1)

for list in lists:
    current_node = list
    while current_node is not None:
        print(current_node, end=' ')
        current_node = current_node.next
    print()

print('\n')



# testing: depth 4
node5 = Node(5)
node4 = Node(4, None, node5)
node3 = Node(3, node4)
node2 = Node(2, None, node3)
node1 = Node(1, None, node2)

lists = list_of_depths(node1)

for list in lists:
    current_node = list
    while current_node is not None:
        print(current_node, end=' ')
        current_node = current_node.next
    print()


