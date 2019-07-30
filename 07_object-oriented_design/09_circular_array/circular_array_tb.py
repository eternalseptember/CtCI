from circular_array import *


def print_queue_status(queue):
    q_full = queue.is_full()
    q_empty = queue.is_empty()
    print('Queue full? {0}'.format(q_full))
    print('Queue empty? {0}'.format(q_empty))


queue_1 = CircularArray(10)
queue_1.enqueue(3)
queue_1.enqueue(1)
queue_1.enqueue(4)
print(queue_1)


"""
queue_1.enqueue(1)
queue_1.enqueue(5)
queue_1.enqueue(9)
queue_1.enqueue(2)
queue_1.enqueue(6)
queue_1.enqueue(5)
queue_1.enqueue(3)
queue_1.enqueue(5)
queue_1.enqueue(8)
print(queue_1)


# should be neither full nor empty
print_queue_status(queue_1)

# should be full
queue_1.enqueue(9)
print_queue_status(queue_1)

# should be empty
queue_1.clear()
print(queue_1)
"""

# START NEW QUEUES FOR EACH TEST CASE

item = queue_1.dequeue()
print('item pulled: {0}'.format(item))
print(queue_1)

# pull remaining two items and then add. where is the new item?
queue_1.dequeue()
queue_1.dequeue()
queue_1.enqueue('A')
print(queue_1)


# should wrap around
queue_1.enqueue('B')
queue_1.enqueue('C')
queue_1.enqueue('D')
queue_1.enqueue('E')
queue_1.enqueue('F')
queue_1.enqueue('G')
queue_1.enqueue('H')
print('queue should wrap around')
print(queue_1)

# what happens when full?
print('what happens when queue is full?')
queue_1.enqueue('I')
queue_1.enqueue('J') # not adding?
print(queue_1)

#
queue_1.enqueue('K')
print(queue_1)


