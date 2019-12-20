"""
Design and implement a hash table which uses chaining (linked lists) to handle
collisions.
"""


class Hash_Table():
    def __init__(self, size):
        self.size = size
        self.linked_list = [None] * size


    def __str__(self):
        table = ''

        for item in self.linked_list:
            if len(table) > 0:
                table += ', '
            table += '{0}'.format(item)

        return table


    def hash(self, item):
        # Hash the key and figure out its address.
        # Given a name, add up the ascii value of the letters,
        # then get the remainder.

        ascii_total = 0
        for letter in list(item):
            ascii_total += ord(letter)

        return ascii_total % self.size


    def get_hash(self):
        # given a key, return the value
        print()

    def insert(self, key, value):
        # get the location by hashing the key
        array_loc = self.hash(key)
        # how to store?
        # collision!
        self.linked_list[array_loc] = value



class Node():
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node




