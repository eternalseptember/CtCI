"""
Given two (singly) linked lists, determine if the two lists intersect.
Return the intersecting node. Note that the intersection is defined
based on reference, not value. That is, if the kth node of the first
linked list is the exact same node (by reference) as the jth node of
the second linked list, then they are intersecting.
"""


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def print_linked_list(head):
    print(head.data, end=' ')
    if head.next is not None:
        print_linked_list(head.next)


def is_intersected(head1, head2):
    # two intersecting linked list will have the same last node
    node_1 = head1
    while node_1.next is not None:
        node_1 = node_1.next

    node_2 = head2
    while node_2.next is not None:
        node_2 = node_2.next

    return node_1 == node_2


def find_intersection(head1, head2):
    # O(A+B) time, where A and B are the lengths of the two linked lists.
    # O(1) additional space
    nodes_list = []
    found = False
    node_intersection = None

    # indexes all nodes from head1
    current_node = head1
    while current_node is not None:
        nodes_list.append(current_node)
        current_node = current_node.next

    # search through head2 for intersection
    current_node = head2
    while current_node is not None:
        if current_node in nodes_list:
            if found is False:
                found = True
                node_intersection = current_node
            else:
                # double check that it was really an intersection
                if current_node not in nodes_list:
                    print('false positive somewhere')

        current_node = current_node.next

    return node_intersection

