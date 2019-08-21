# Solution.


class CircularArray():
    def __init__(self, size):
        self.size = size
        self.items = [None for item in range(size)]
        self.head = 0

    def convert(self, index):
        if (index < 0):
            index += self.size

        return (self.head + index) % self.size



