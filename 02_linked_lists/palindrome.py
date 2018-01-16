"""
Implement a function to check if a linked list is a palindrome.
"""


class Node:
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


def is_palindrome(head):
    string = []

    while head is not None:
        string.append(head.data)
        head = head.next

    while len(string) >= 2:
        item1 = string.pop(0)
        item2 = string.pop()

        if item1 != item2:
            return False

    return True


def test_palindrome_function(test_str):
    head = None
    values = []

    for ch in test_str:
        values.append(ch)

    for value in values:
        head = add(head, value)

    result = is_palindrome(head)
    print(result)


# Test cases:
# True, True, True, True, False, False
test_cases = ['racecar', 'mom', 'noon', 'toot', 'cat', 'plop']

for case in test_cases:
    test_palindrome_function(case)
