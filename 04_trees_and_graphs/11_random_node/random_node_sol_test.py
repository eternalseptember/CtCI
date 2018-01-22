# Testing the provided solution for the random node problem.


from random_node_sol import *


# Example tree from solutions manual

# How does insert function work?
# nodes_list = [10, 5, 15, 17, 3, 7, 20, 30]

# This is the tree in the example:
nodes_list = [20, 10, 30, 5, 3, 7, 15, 17]

head = None

for val in nodes_list:
    if head is None:
        head = Node(val)
    else:
        head.insert_in_order(val)


print_tree(head)

# Testing find function
# Finding the head
print('\n\n\tHead node found?')
found = head.find(20)
print(found)


# Left of the tree
print('\tFind something to the left of the root:')
# True
found = head.find(7)
print(found)

# False/None
found = head.find(18)
print(found)


# Right of the tree
print('\tFind something to the right of the root:')
# True
found = head.find(30)
print(found)

# False/None
found = head.find(25)
print(found)


print('\nRandom node:')
random_node = head.get_random_node()
print(random_node)


