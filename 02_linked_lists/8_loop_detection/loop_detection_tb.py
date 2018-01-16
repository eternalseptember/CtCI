# Test cases for the "loop detection" problem.


from loop_detection import *


# Expected result: C
values = ['A', 'B', 'C', 'D', 'E']
head = None
latest_node = None
loop_node = None

for value in values:
    head, latest_node = add(head, value)

    if value == 'C':
        loop_node = latest_node

# make a loop
latest_node.next = loop_node

# normally I'd print the node here, but recursion

print('Node at the beginning of loop: ')
beg_loop_node = detect_loop(head)
if beg_loop_node is not None:
    print(beg_loop_node.data)
else:
    print('No loop detected.')
print()



# Does this function work for non-circular loops?
# Expected result: C
values = ['A', 'B', 'C', 'D', 'E']
head = None
latest_node = None

for value in values:
    head, latest_node = add(head, value)

print('Node at the beginning of loop: ')
beg_loop_node = detect_loop(head)
if beg_loop_node is not None:
    print(beg_loop_node.data)
else:
    print('No loop detected.')
print()

