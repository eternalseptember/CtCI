"""
Implement a CircularArray class that supports an array-like data structure
which can be efficiently rotated. IF possible, the class should use a generic
type (also called a template), and should support iteration via the standard
for (Obj o : circularArray) notation.
"""


class CircularArray:
    def __init__(self, items):
        self.items = items

