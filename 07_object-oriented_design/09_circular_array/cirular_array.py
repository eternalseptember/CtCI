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
        self.head = 0
        self.tail = 0


    def __str__(self):
        item_list = ''
        for item in self.queue:
            # when to insert ocmma
            item_list += str(item)

        return item_list


    def enqueue(self, item):
        # figure out where heads and tails are

        self.tail += 1
        if self.tail >= self.tail:
            self.tail = 0

        return None


    def dequeue(self):
        # Remove item at the beginning of the queue.
        # return the item that was popped
        item = self.queue[self.head]

        # might have to loop back
        self.head += 1
        if self.head >= self.size:
            self.head = 0

        return item


    def rotate(self):
        return None

