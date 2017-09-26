"""
Implement a MyQueue class which implements a queue using two stacks.
"""


class MyQueue:
    def __init__(self):
        self.newest_stack = []
        self.oldest_stack = []


    def print_oldest_queue(self):
        print(str(self.oldest_stack))


    def print_newest_queue(self):
        print(str(self.newest_stack))


    def size(self):
        return len(self.newest_stack) + len(self.oldest_stack)


    def add(self, item):
        self.newest_stack.append(item)


    def remove(self):
        self.move_to_oldest_stack()

        try:
            return self.oldest_stack.pop()
        except:
            return None


    def move_to_oldest_stack(self):
        if len(self.oldest_stack) == 0:
            while len(self.newest_stack) > 0:
                item = self.newest_stack.pop()
                self.oldest_stack.append(item)


    def peek(self):
        self.move_to_oldest_stack()
        try:
            return self.oldest_stack[-1]
        except IndexError:
            return None


    def is_empty(self):
        if (len(self.newest_stack) > 0) or (len(self.oldest_stack) > 0):
            return False
        else:
            return True


# testing

test_op = ['push', 'push', 'push', 'push', 'pop']
test_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_queue = MyQueue()

for op in test_op:
    if op == 'push':
        print('Add')

        value = test_values.pop(0)
        test_queue.add(value)
    
    elif op == 'pop':
        print('Dequeue')

        popped_item = test_queue.remove()
        # print('popped item: {0}'.format(popped_item))


    # After performing the operations, print queue info.
    print('--------------------------------------------')
    print('Queue is empty? \t\t{0}'.format(test_queue.is_empty()))
    print('Queue size: \t\t\t{0}'.format(test_queue.size()))
    print('Front of queue: \t\t{0}'.format(test_queue.peek()))
    print('Newest queue: \t\t\t', end='')
    test_queue.print_newest_queue()
    print('Oldest queue: \t\t\t', end='')
    test_queue.print_oldest_queue()


    print('\n')





