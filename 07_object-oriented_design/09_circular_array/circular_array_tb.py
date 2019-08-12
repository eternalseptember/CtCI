from circular_array import *


def print_queue_status(queue):
    print(queue)
    q_full = queue.is_full()
    q_empty = queue.is_empty()
    print('\tQueue full? {0}'.format(q_full))
    print('\tQueue empty? {0}'.format(q_empty))
    print()


# Test case 1
print('=== Test Case 1 ===')
print('=== Initialized queue should be empty. ===')
queue_1 = CircularArray(6)
print_queue_status(queue_1)

# adding items
queue_1.enqueue(0)
queue_1.enqueue(1)
queue_1.enqueue(2)
queue_1.enqueue(3)
queue_1.enqueue(4)

print('=== Queue should be neither full nor empty. ===')
print_queue_status(queue_1)

print('=== Queue should be full. ===')
queue_1.enqueue(5)
print_queue_status(queue_1)  # not returning the correct answer

print('=== Queue should be empty. ===')
queue_1.clear()
print_queue_status(queue_1)


print()
print('=== Test Case 2 ===')
queue_2 = CircularArray(8)
queue_2.enqueue(1)
queue_2.enqueue(2)
queue_2.enqueue(3)
queue_2.enqueue(4)

print('=== Four items. ===')
print_queue_status(queue_2)

print('=== Queue should have one less item. ===')
item = queue_2.dequeue()
print('Item dequeued: {0}'.format(item))
print_queue_status(queue_2)

print('=== Add an item. ===')
queue_2.enqueue(5)
print_queue_status(queue_2)


# Full first, then dequeue...

"""
item = queue_2.dequeue()
print('item pulled: {0}'.format(item))
print(queue_2)

# pull remaining two items and then add. where is the new item?
queue_2.dequeue()
queue_2.dequeue()
queue_2.enqueue('A')
print(queue_2)


# should wrap around
queue_2.enqueue('B')
queue_2.enqueue('C')
queue_2.enqueue('D')
queue_2.enqueue('E')
queue_2.enqueue('F')
queue_2.enqueue('G')
queue_2.enqueue('H')
print('queue should wrap around')
print(queue_2)

# what happens when full?
print('what happens when queue is full?')
queue_2.enqueue('I')
queue_2.enqueue('J')  # not adding?
print(queue_2)

#
queue_2.enqueue('K')
print(queue_2)
"""



