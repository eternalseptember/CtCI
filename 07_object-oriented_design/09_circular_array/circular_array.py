"""
Implement a CircularArray class that supports an array-like data structure
which can be efficiently rotated. If possible, the class should use a generic
type (also called a template), and should support iteration via the standard
for (Obj o : circularArray) notation.
"""

# The rotate() method should be able to run in O(1) time.


class CircularArray:
    def __init__(self, size):
        self.size = size
        self.queue = [None for item in range(size)]
        self.num_of_items = 0
        self.head = 0
        self.tail = 0


    def __str__(self):
        item_list = ''
        for item in self.queue:
            if len(item_list) > 0:
                item_list += ', '
            item_list += str(item)

        return item_list


    def __repr__(self):
        item_list = ''
        for item in self.queue:
            if len(item_list) > 0:
                item_list += ', '
            item_list += str(item)

        return item_list


    def enqueue(self, item):
        # Put item at the tail end.
        if self.is_full():
            print('queue is full')
            return None
        else:
            self.queue[self.tail] = item
            self.rotate(self.tail)
            # self.tail = (self.tail + 1) % self.size
            self.num_of_items += 1


    def dequeue(self):
        # Remove item at the beginning of the queue.
        # return the item that was popped
        if self.is_empty():
            return None
        else:
            item = self.queue[self.head]
            self.queue[self.head] = None
            self.rotate(self.head)
            # self.head = (self.head + 1) % self.size
            self.num_of_items -= 1
            return item


    def is_empty(self):
        if self.num_of_items == 0:
            return True
        else:
            return False


    def is_full(self):
        if self.num_of_items == self.size:
            return True
        else:
            return False


    def clear(self):
        self.queue = [None for item in range(self.size)]
        self.head = 0
        self.tail = 0


    def rotate(self, pointer):
        # going to the next index
        # pointer should be self.head or self.tail
        pointer = (pointer + 1) % self.size




