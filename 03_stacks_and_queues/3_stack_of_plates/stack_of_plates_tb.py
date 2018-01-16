# Test cases for the "stack of plates" problem.


from stack_of_plates import *


# Initial stack setup
values_to_test = [2, 5, 2, 1, 5, 7, 3, 8, 1, 9, 8, 3, 4, 6, 4, 5, 0, 9, 2]
stack_set = SetOfStacks()

for value in values_to_test:
    stack_set.push(value)

print('Initial stack:')
print(stack_set)
print()


# Testing popAt function
# Exhausting the last stack, then popAt the last-stack after it's empty
# requested_stacks = [0, 0, 3, 3, 3, 3]

# Exhausting the last stack and popAt second-to-last stack
# requested_stacks = [0, 0, 3, 3, 2]

# Exhausting a stack in the middle
requested_stacks = [1, 1, 1, 1, 1]

for stack_number in requested_stacks:
    stack_set.popAt(stack_number)
    print('Pop a plate from stack: {0}'.format(stack_number))
    print(stack_set)
print()

"""
# Testing a final pop function
print('Final pop')
stack_set.pop()
print(stack_set)
"""

# Testing a final add
print('Final add')
final_add_values = [100, 101]

for value in final_add_values:
    stack_set.push(value)
    print(stack_set)



