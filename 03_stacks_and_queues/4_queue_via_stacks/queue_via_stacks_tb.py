# Test cases for the "queue via stacks" problem.


from queue_via_stacks import *


# 4 push, 2 pop, 2 push, 4 pop => queue should be zero
# 3 push, 1 pop, 2 push, 1 pop => queue should have 3 remaining
# push, pop, push, pop => alternating push and pop
# 3 push => queue should have 6 remaining
test_op = ['push', 'push', 'push', 'push', 'pop', 'pop', 'push', 'push', 'pop', 'pop', 'pop', 'pop', 'push', 'push', 'push', 'pop', 'push', 'push', 'pop', 'push', 'pop', 'push', 'pop', 'push', 'push', 'push']
test_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
test_queue = MyQueue()

for op in test_op:
    if op == 'push':
        print('Add')

        value = test_values.pop(0)
        test_queue.add(value)
    
    elif op == 'pop':
        print('Dequeue')

        popped_item = test_queue.remove()
        # print('popped item: {0}'.format(popped_item))


    # After performing the operations, print queue info.
    print('--------------------------------------------')
    print('Newest queue: \t\t\t', end='')
    test_queue.print_newest_queue()
    print('Oldest queue: \t\t\t', end='')
    test_queue.print_oldest_queue()

    print('Queue is empty? \t\t{0}'.format(test_queue.is_empty()))
    print('Queue size: \t\t\t{0}'.format(test_queue.size()))
    print('Front of queue: \t\t{0}'.format(test_queue.peek()))

    print('\n')


print('\nFinal queue info:')
print('--------------------------------------------')
print('Newest queue: \t\t\t', end='')
test_queue.print_newest_queue()
print('Oldest queue: \t\t\t', end='')
test_queue.print_oldest_queue()
print('Queue is empty? \t\t{0}'.format(test_queue.is_empty()))
print('Queue size: \t\t\t{0}'.format(test_queue.size()))
print('Front of queue: \t\t{0}'.format(test_queue.peek()))

