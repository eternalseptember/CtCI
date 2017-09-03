"""
Write a program to sort a stack such that the smallest items are on top.
You can use an additional temporary stack, but you may not copy the
elements into any other data structure (such as array). The stack supports
the following operations: push, pop, peek, and isEmpty().
"""

class Stack:
    def __init__(self):
        self.stack = []


    def push(self, item):
        self.stack.append(item)


    def pop(self):
        item = self.stack.pop()
        return item


    def peek(self):
        return self.stack[-1]


    def is_empty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True

    def __str__(self):
        return str(self.stack)


def sort(unsorted_stack):
    # larger items are at the bottom
    sorted_stack = Stack()
    
    while unsorted_stack.is_empty() is False:
        item = unsorted_stack.pop()

        if (sorted_stack.is_empty()) or (item <= sorted_stack.peek()):
            sorted_stack.push(item)
        else:
            num_transferred = 0

            # find the place to insert the item
            while (sorted_stack.is_empty() is False) and (item > sorted_stack.peek()):
                transfer_item = sorted_stack.pop()
                unsorted_stack.push(transfer_item)
                num_transferred += 1

            # insert the item
            sorted_stack.push(item)

            # move the items back to the sorted stack
            while num_transferred > 0:
                transfer_item = unsorted_stack.pop()
                sorted_stack.push(transfer_item)
                num_transferred -= 1

    return sorted_stack


# testing
values_to_add = [1, 2, 7, 5, 9, 0, 3, 2, 7, 6, 6, 8]

stack = Stack()
for value in values_to_add:
    stack.push(value)

print('Unsorted stack:')
print(stack)

sorted_stack = sort(stack)
print('Sorted stack:')
print(sorted_stack)


