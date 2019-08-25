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


    def rotate(self, index):
        self.head = self.convert(index)


    def get(self, index):
        if (index < 0) or (index >= self.size):
            # return an exception
            return None


    def set(self, index, item):
        self.items[self.convert(index)] = item



