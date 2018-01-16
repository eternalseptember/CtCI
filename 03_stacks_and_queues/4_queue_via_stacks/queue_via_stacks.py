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
        except IndexError:
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

