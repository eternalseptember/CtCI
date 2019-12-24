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

        """
        for item in self.linked_list:
            if len(table) > 0:
                table += ', '
            table += '{0}'.format(item)
        """

        for index in range(self.size):
            item = self.linked_list[index]

            if len(table) > 0:
                table += '\n'

            if item is None:
                table += 'None'
            else:
                # print through the linked list on one line
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


    def get_hash(self):
        # given a key, return the value
        print()

    def insert(self, key, value):
        # get the location by hashing the key
        array_loc = self.hash(key)
        # how to store?
        # collision!
        new_node = Node(value)

        if self.linked_list[array_loc] is None:
            self.linked_list[array_loc] = new_node
        else:
            # else add new node at the end of the chained list
            current_node = self.linked_list[array_loc]
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node



class Node():
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


    def __str__(self):
        return str(self.data)




