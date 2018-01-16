# Test cases for "minimal tree" problem.


from minimal_tree import *


# Test case 1: odd number of elements
# root of the tree: 5, left: 2, right: 8
list_of_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

head = create_minimal_tree(list_of_values)
print('Odd number of elements')
print_tree(head)
print()


# Test case 2: even number of elements
list_of_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

head = create_minimal_tree(list_of_values)
print('Even number of elements')
print_tree(head)
print()





