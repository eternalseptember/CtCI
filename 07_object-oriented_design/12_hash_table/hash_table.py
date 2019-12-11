"""
Design and implement a hash table which uses chaining (linked lists) to handle
collisions.
"""


class Hash_Table():
    def __init__(self, size):
        self.size = size
        self.linked_list = []


    def hash(self, item):
        # hash the key and figure out its address
        # testing with numeric keys
        array_loc = item % self.size
        return array_loc


    def get_hash(self):
        # given a key, return the value
        print()

    def insert(self, key, value):
        # get the location by hashing the key
        array_loc = self.hash(key)
        # how to store?



class Node():
    def __init__(self, data):
        self.data = data




