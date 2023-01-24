# Test cases for the "sort stack" problem.


from sort_stack import *


values_to_add = [1, 2, 7, 5, 9, 0, 3, 2, 7, 6, 6, 8]

stack = Stack()
for value in values_to_add:
	stack.push(value)

print('Unsorted stack:')
print(stack)

sorted_stack = sort(stack)
print('Sorted stack:')
print(sorted_stack)

