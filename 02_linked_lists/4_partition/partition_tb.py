# Test cases for the "partition" problem.


from partition import *


# Expected result: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
x = 5

values = [3, 5, 8, 5, 10, 2, 1]
head = None

for value in values:
	head = add(head, value)

print('linked list adding all nodes:')
print_linked_list(head)
print()

print('linked list after partitioning:')
partitioned_head = partition(head, x)
print_linked_list(partitioned_head)

