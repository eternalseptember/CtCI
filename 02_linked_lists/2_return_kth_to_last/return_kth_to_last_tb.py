# Test cases for "return kth to last" problem.


from return_kth_to_last import *


values = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
head = None

for value in values:
    head = add(head, value)

print('linked list adding all nodes:')
print_linked_list(head)
print()

k = 2
result = find_element(k, head)
print('{0}-to-last element in linked list:'.format(k))
print(result.data)

