"""
Imagine a (literal) stack of plates. If the stack gets too high, it might
topple. Therefore, in real life, we would likely start a new stack when the
previous stack exceeds some threshold. Implement a data structure
SetOfStacks that mimics this. SetOfStacks should be composed of several
stacks and should create a new stack once the previous one exceeds capacity.
SetsOfStacks.push() and SetOfStacks.pop() should behave identically to a
single stack (that is, pop() should return the same values as it would if
there were just a single stack).

Implement a function popAt(int index) which performs a pop operation on a
specific sub-stack.
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
            self.set_of_stacks.append([])

        # add the item to the stack
        self.set_of_stacks[self.current_stack].append(item)


    def pop(self):
        # if current stack is empty, go to the previous stack
        if len(self.set_of_stacks[self.current_stack]) == 0:
            self.current_stack -= 1
            self.set_of_stacks.pop()

        # check if all stack is empty
        if (self.current_stack == 0) and len(self.set_of_stacks[0] == 0):
            return None
        else:
            return self.set_of_stacks[self.current_stack].pop()


    def popAt(self, requested_stack):
        if requested_stack <= self.current_stack:
            if len(self.set_of_stacks[requested_stack]) > 0:
                requested_item = self.set_of_stacks[requested_stack].pop()

                # Roll over items from newer stack
                # Increases time complexity
                this_stack = requested_stack

                while this_stack < self.current_stack:
                    next_stack = this_stack + 1
                    transfer_item = self.set_of_stacks[next_stack].pop(0)
                    self.set_of_stacks[this_stack].append(transfer_item)

                    this_stack = next_stack

                return requested_item


        return None


    def __str__(self):
        return str(self.set_of_stacks)



# Testing
# Initial stack setup
values_to_test = [2, 5, 2, 1, 5, 7, 3, 8, 1, 9, 8, 3, 4, 6, 4, 5, 0, 9, 2]
stack_set = SetOfStacks()

for value in values_to_test:
    stack_set.push(value)

print('Initial stack:')
print(stack_set)
print()

# Testing popAt function
requested_stacks = [0, 0, 3]

for stack_number in requested_stacks:
    stack_set.popAt(stack_number)
    print('Pop a plate from stack: {0}'.format(stack_number))
    print(stack_set)

