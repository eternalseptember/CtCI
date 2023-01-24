# Test case for "remove dups" problem.


from remove_dups import *


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


