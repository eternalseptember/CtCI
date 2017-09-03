"""
Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?
"""


class Node:
    # def __init__(self, data=None, prev=None, next_node=None):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def print_linked_list(head):
    print(head.data, end=' ')
    if head.next is not None:
        print_linked_list(head.next)


def add(head, value):
    if head is None:
        return Node(value)

    if head.next is None:
        head.next = Node(value)
    else:
        next_node = head.next
        while next_node.next is not None:
            next_node = next_node.next
        next_node.next = Node(value)

    return head


"""
def remove_duplicates(head):
    # this implementation uses a temporary buffer
    # O(N) time, where N is the number of elements in the linked list.
    unique_values = []
    current_head = head
    previous_node = None

    while current_head is not None:
        if current_head.data not in unique_values:
            unique_values.append(current_head.data)
            previous_node = current_head
        else:
            previous_node.next = current_head.next

        current_head = current_head.next

    return head
"""


def remove_duplicates(head):
    # this implementation does not use a temporary buffer
    # Runs in O(1) space but O(N^2) time.
    current_node = head

    while current_node is not None:
        this_node = current_node

        while this_node.next is not None:
            if this_node.next.data == current_node.data:
                this_node.next = this_node.next.next
            else:
                this_node = this_node.next

        current_node = current_node.next

    return head


# Setup for testing
values = [9, 0, 1, 1, 9, 3, 4, 2, 0, 2, 5, 1]
head = None

for value in values:
    head = add(head, value)

print('linked list adding all nodes:')
print_linked_list(head)
print()

head = remove_duplicates(head)
print('linked list after removing duplicates:')
print_linked_list(head)
print()
