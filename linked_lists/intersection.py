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

    # hash table?
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
print()

# Non-intersecting linked lists
# List 1
list_1_a = Node(1)
list_1_b = Node(2, list_1_a)
list_1_c = Node(7, list_1_b)
list_1_d = Node(9, list_1_c)
list_1_e = Node(5, list_1_d)
list_1_f = Node(1, list_1_e)
list_1_g = Node(3, list_1_f)  # head_1


# List 2
list_2_a = Node(1)
list_2_b = Node(2, list_2_a)
list_2_c = Node(7, list_2_b)
list_2_d = Node(6, list_2_c)
list_2_e = Node(4, list_2_d)  # head_2


# testing
head_1 = list_1_g
head_2 = list_2_e
intersection = find_intersection(head_1, head_2)

if intersection is not None:
    print_linked_list(intersection)
else:
    print('No intersection')
print()


"""
if list_1_a == list_2_a:
    print('these two nodes are the same')
else:
    print('these two nodes are different')
"""






