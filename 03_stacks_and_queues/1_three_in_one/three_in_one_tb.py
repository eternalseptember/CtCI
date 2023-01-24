# Test cases for the "three in one" problem.


from three_in_one import *


#values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
values = [1, 2, 3, 4, 5, 6]
three_stack = ThreeStacks()

stack_index = 1
for value in values:
	three_stack.push(value, stack_index)

	stack_index += 1
	if stack_index > 3:
		stack_index = 1


print(three_stack)


stack_index = 1
for i in range(6):
	pop_item = three_stack.pop(stack_index)
	top_item = three_stack.peek(stack_index)
	print('stack: {0}  pop: {1}  top: {2}'.format(stack_index, pop_item, top_item))
	print(three_stack)

	stack_index += 1
	if stack_index > 3:
		stack_index = 1

