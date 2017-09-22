"""
Implement a MyQueue class which implements a queue using two stacks.
"""


class MyQueue:
    def __init__(self):
        self.newest_stack = []
        self.oldest_stack = []


    def add(self, item):
        self.newest_stack.append(item)


    def remove(self):
        # move items to the oldest stack
        while len(self.newest_stack) > 1:
            item = self.newest_stack.pop()
            self.oldest_stack.append(item)

        # the last item is reached
        remove_item = self.newest_stack.pop()

        # put the items back
        while len(self.oldest_stack) > 0:
            item = self.oldest_stack.pop()
            self.newest_stack.append(item)

        return remove_item


    def peek(self):
        try:
            return self.newest_stack[0]
        except IndexError:
            return None


    def is_empty(self):
        if len(self.newest_stack) > 0:
            return False
        else:
            return True


    def __str__(self):
        return str(self.newest_stack)


# testing
test_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_queue = MyQueue()

for value in test_values:
    test_queue.add(value)

print('Test queue: ', end=' ')
print(test_queue)
print()

for i in range(len(test_values)):
    popped_item = test_queue.remove()
    print('popped item: {0}'.format(popped_item))

    queue_front = test_queue.peek()
    print('front of queue: {0}'.format(queue_front))

    print('remaining queue: {0}'.format(test_queue))
    print()


