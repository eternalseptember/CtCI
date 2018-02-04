# Testing option 7.


from random_node_sol_2 import *


# Example tree from solutions manual
nodes_list = [20, 10, 30, 5, 3, 7, 15, 17]


head = Tree()

for val in nodes_list:
    head.insert_in_order(val)
    print('size of tree: {0}'.format(head.get_size()))


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


