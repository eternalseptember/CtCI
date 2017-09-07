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


def find_intersection(head1, head2):
    # assumes that there is an intersection
    orig_head2 = head2

    while head1 is not None:
        while head2 is not None:
            if head1.next is None:
                head_1_next = None
            else:
                head_1_next = head1.next

            if head2.next is None:
                head_2_next = None
            else:
                head_2_next = head2.next


            if (head1.data == head2.data) and (head_1_next == head_2_next):
                return head2
            head2 = head2.next
        head1 = head1.next
        head2 = orig_head2

    return None


# Test cases
# Intersecting linked list
linked_node_a = Node(1)
linked_node_b = Node(2, linked_node_a)
linked_node_c = Node(7, linked_node_b)

linked_node_d = Node(9, linked_node_c)
linked_node_e = Node(5, linked_node_d)
linked_node_f = Node(1, linked_node_e)
linked_node_g = Node(3, linked_node_f)  # head_1

linked_node_h = Node(6, linked_node_c)
linked_node_i = Node(4, linked_node_h)  # head_2

head_1 = linked_node_g
head_2 = linked_node_i
intersection = find_intersection(head_1, head_2)

if intersection is not None:
    print_linked_list(intersection)
else:
    print('No intersection')


# Non-intersecting linked lists
# List 1
list_1_a = Node(1)
list_1_b = Node(2, list_1_a)
list_1_c = Node(7, list_1_b)
list_1_d = Node(9, list_1_c)
list_1_e = Node(5, list_1_d)
list_1_f = Node(1, list_1_e)
list_1_e = Node(3, list_1_f)



# List 2










