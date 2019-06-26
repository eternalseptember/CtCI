"""
Implement a CircularArray class that supports an array-like data structure
which can be efficiently rotated. If possible, the class should use a generic
type (also called a template), and should support iteration via the standard
for (Obj o : circularArray) notation.
"""

# The rotate() method should be able to run in O(1) time.


class CircularArray:
    def __init__(self, size):
        self.queue = [None for item in range(size)]


    def add(self, item):
        # figure out where heads and tails are
        return None


    def rotate(self):
        return None

