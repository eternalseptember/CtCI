# Test cases for random node problem.


from random_node import *


# testing
values = [7, 5, 3, 8, 1, 8, 0, 2, 5, 2, 4, 1]
# values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
head = None

for value in values:
    head = insert(head, value)

print('original tree')
print_level_order(head)
print()


"""
# test case 1: true
node2 = Node(2)
node4 = Node(4)
look_for_this_node = Node(1, node2, node4)

found_node, found_head = find(head, look_for_this_node)
print(found_node)


# test case 2: true
look_for_this_node = Node(2)

found_node, found_head = find(head, look_for_this_node)
print(found_node)


# test case 3: false
look_for_this_node = Node(7)

found_node, found_head = find(head, look_for_this_node)
print(found_node)


# test case 4: false
node0 = Node(0)
node4 = Node(4)
look_for_this_node = Node(1, node0, node4)

found_node, found_head = find(head, look_for_this_node)
print(found_node)


# test case 5: false
node4 = Node(4)
look_for_this_node = Node(1, None, node4)

found_node, found_head = find(head, look_for_this_node)
print(found_node)


# test case 6: true
node1 = Node(1)
look_for_this_node = Node(8, node1)

found_node, found_head = find(head, look_for_this_node)
print(found_node)
"""


# test 1 delete: false
node5 = Node(5)
node2 = Node(2)
target_node = Node(7, node5, node2)

delete_success = delete(head, target_node)
if delete_success is not None:
    print_level_order(delete_success)
else:
    print(delete_success)
print()


# test 2 delete: true, deleting leaf
target_node = Node(1)

delete_success = delete(head, target_node)
if delete_success is not None:
    print_level_order(delete_success)
else:
    print(delete_success)
print()


# test 3 delete: true, deleting root
node5 = Node(5)
node3 = Node(3)
target_node = Node(7, node5, node3)

delete_success = delete(head, target_node)
if delete_success is not None:
    print_level_order(delete_success)
else:
    print(delete_success)
print()


# test 4 delete: true, deleting middle leaf, left has lower value
node2 = Node(2)
node4 = Node(4)
target_node = Node(1, node2, node4)

delete_success = delete(head, target_node)
if delete_success is not None:
    print_level_order(delete_success)
else:
    print(delete_success)
print()


# test 5 delete: true, deleting middle leaf, right has lower value
node8 = Node(8)
node1 = Node(1)
target_node = Node(5, node8, node1)

delete_success = delete(head, target_node)
if delete_success is not None:
    print_level_order(delete_success)
else:
    print(delete_success)
print()



"""
# test 1 random node:
for i in range(15):
    random_node = get_random_node(head)
    print(random_node)
    print()
"""
