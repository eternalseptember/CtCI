"""
How would you design a stack which, in addition to push and pop,
has a function min which returns the minimum element? Push, pop,
and min should all operate in O(1) time.
"""


class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, item):
        self.stack.append(item)

        if len(self.min_stack) == 0:
            self.min_stack.append(item)
        else:
            if item <= self.min_stack[-1]:
                self.min_stack.append(item)


    def pop(self):
        item = self.stack.pop()

        if item == self.min_stack[-1]:
            self.min_stack.pop()

        return item


    def peek(self):
        try:
            return self.stack[-1]
        except IndexError:
            return None



    def is_empty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True


    def print_min(self):
        try:
            print(self.min_stack[-1])
        except IndexError:
            print('No minimum')


# Test
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

