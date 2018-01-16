# Test cases for the "stack min" problem.


from stack_min import *


# values_to_add = [5, 6, 1, 2, 8, 0, 9]
values_to_add = [5, 6, 3, 7]

new_stack = Stack()
for value in values_to_add:
    new_stack.push(value)
    new_stack.print_min()

print()
for i in range(4):
    new_stack.pop()
    new_stack.print_min()

