# Test cases for the "delete middle node" problem.


from delete_middle_node import *


values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
head = None
delete_this_node = None

for value in values:
    head, new_node = add(head, value)

    # set a value for testing
    if value == 4:
        delete_this_node = new_node


print('linked list adding all nodes:')
print_linked_list(head)
print()

print('linked list starting at the node to be deleted:')
print_linked_list(delete_this_node)
print()

delete_node(delete_this_node)
print('linked list after deleting a middle node:')
print_linked_list(head)
print()

