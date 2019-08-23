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


    def get(self):
        return None


    def set(self, item):
        return None



