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

queue_1.clear()
print(queue_1)

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


