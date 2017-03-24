"""
Imagine a (literal) stack of plates. If the stack gets too high, it might
topple. Therefore, in real life, we would likely start a new stack when the
previous stack exceeds some threshold. Implement a data structure
SetOfStacks that mimics this. SetOfStacks should be composed of several
stacks and should create a new stack once the previous one exceeds capacity.
SetsOfStacks.push() and SetOfStacks.pop() should behave identically to a
single stack (that is, pop() should return the same values as it would if
there were just a single stack).
"""


class SetOfStacks:
	def __init__(self, threshold=5):
		self.threshold = threshold
		self.set_of_stacks = [[]]
		self.current_stack = 0

	def push(self, item):
		# if current stack is full, create a new stack
		if len(self.set_of_stacks[self.current_stack]) == self.threshold:
			self.current_stack += 1
			new_stack = [item]
			self.set_of_stacks.append(new_stack)
		else:
			self.set_of_stacks[self.current_stack].append(item)

	def pop(self):
		if len(self.set_of_stacks[self.current_stack] == 0):
			self.current_stack -= 1
		# check if all stack is empty
		# return item

	def __str__(self):
		return str(self.set_of_stacks)



# testing
values_to_test = [2, 5, 2, 1, 5, 7, 3, 8, 1, 9, 8, 3, 4, 6, 4, 5, 0, 9, 2]
stack_set = SetOfStacks()

for value in values_to_test:
	stack_set.push(value)

print(stack_set)

