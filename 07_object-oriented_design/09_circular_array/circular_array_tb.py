from circular_array import *


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
# one left
