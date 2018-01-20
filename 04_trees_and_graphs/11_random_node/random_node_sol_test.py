# Testing the provided solution for the random node problem.


from random_node_sol import *


# Example tree from solutions manual

# nodes_list = [5, 3, 7]
nodes_list = [10, 5, 15, 17, 3, 7, 20, 30]

head = None

for val in nodes_list:
    if head is None:
        head = Node(val)
    else:
        head.insert_in_order(val)


# print_tree(head)

# Testing find function
# False/None
found = head.find(18)
print(found)

# True
found = head.find(20)
print(found)
