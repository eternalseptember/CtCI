from circular_array import *


def print_queue_status(queue):
    print(queue)
    q_full = queue.is_full()
    q_empty = queue.is_empty()
    print('\tQueue full? {0}'.format(q_full))
    print('\tQueue empty? {0}'.format(q_empty))
    print()


def dequeue(queue):
    item = queue.dequeue()
    print('Item dequeued: {0}'.format(item))
    print_queue_status(queue)


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
dequeue(queue_2)

print('=== Dequeue some more. ===')
dequeue(queue_2)
dequeue(queue_2)

print('=== Add until it wraps around. ===')
queue_2.enqueue(5)
queue_2.enqueue(6)
queue_2.enqueue(7)
queue_2.enqueue(8)
print_queue_status(queue_2)

# reset head and tail when empty?

print('=== Wraps around. ===')
queue_2.enqueue(9)
print_queue_status(queue_2)

print('=== What happens when queue is full? ===')
queue_2.enqueue(10)
queue_2.enqueue(11)
print_queue_status(queue_2)

print('=== Dequeing from a full queue. ===')
dequeue(queue_2)






