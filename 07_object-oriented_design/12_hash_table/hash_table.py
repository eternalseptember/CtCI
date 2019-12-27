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

        for index in range(self.size):
            # Each item in the array gets its own line.
            item = self.linked_list[index]

            if len(table) > 0:
                table += '\n'

            if item is None:
                table += 'None'
            else:
                # Print through the linked list on one line.
                line = str(item)

                current_node = item
                while current_node.next is not None:
                    line += ', '
                    current_node = current_node.next
                    line += str(current_node)

                table += line

        return table


    def hash(self, item):
        # Hash the key and figure out its address.
        # Given a name, add up the ascii value of the letters,
        # then get the remainder.
        ascii_total = 0
        for letter in list(item):
            ascii_total += ord(letter)

        return ascii_total % self.size


    def insert(self, key, value):
        # get the location by hashing the key
        array_loc = self.hash(key)
        # how to store?
        # collision!
        new_node = Node(key, value)


        if self.linked_list[array_loc] is None:
            # If this is the first item at this array location.
            self.linked_list[array_loc] = new_node
        else:
            # Else, add new node at the end of the chained list.
            current_node = self.linked_list[array_loc]
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node


    def get(self):
        # given a key, return the value
        print()


    def delete(self, key):
        # given key, delete value?

        # get the hash
        array_loc = self.hash(key)
        item = self.linked_list[array_loc]

        # if the hash location already has nothing in it

        # if there's only one item left in the location, reset to None
        
        print()


class Node():
    def __init__(self, key, value, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node


    def __str__(self):
        return '({0}: {1})'.format(self.key, self.value)




