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
        # Get the location by hashing the key.
        array_loc = self.hash(key)
        new_node = Node(key, value)

        # Handle collisions with chaining.
        if self.linked_list[array_loc] is None:
            # If this is the first item at this array location.
            self.linked_list[array_loc] = new_node
        else:
            # Check to see if the node needs to be updated.
            # Otherwise, add new node at the end of the chained list.
            current_node = self.linked_list[array_loc]

            if current_node.key == key:
                current_node.value = value
            else:
                add_node = True
                while current_node.next is not None:
                    current_node = current_node.next

                    if current_node.key == key:
                        current_node.value = value
                        add_node = False
                        break

                if add_node:
                    current_node.next = new_node


    def get(self, key):
        # Return the value for the key.
        array_loc = self.hash(key)
        current_node = self.linked_list[array_loc]

        if current_node is None:
            return None
        else:
            # Loop through the chain.
            if current_node.key == key:
                return current_node.value
            while current_node.next is not None:
                current_node = current_node.next

                if current_node.key == key:
                    return current_node.value

            return None


    def delete(self, key):
        # Returns True if delete was successful.
        array_loc = self.hash(key)
        current_node = self.linked_list[array_loc]

        if current_node is None:
            # This entry does not exist.
            return False
        else:
            # still return False if entry is not within linked list
            if current_node.key == key:
                self.linked_list[array_loc] = current_node.next
                return True
            else:
                while current_node is not None:
                    prev_node = current_node
                    current_node = current_node.next

                    if current_node.key == key:
                        prev_node.next = current_node.next
                        return True

                return False



class Node():
    def __init__(self, key, value, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node


    def __str__(self):
        return '({0}: {1})'.format(self.key, self.value)




