# Testing option 7.


from random_node_sol_2 import *


# Example tree from solutions manual
nodes_list = [20, 10, 30, 5, 3, 7, 15, 17]


head = Tree()

for val in nodes_list:
    head.insert_in_order(val)


print_tree(head)

