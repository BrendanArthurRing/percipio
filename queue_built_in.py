import queue

# initialize queue
q = queue.Queue()

# Check queue
q.queue # deque([])

# Add 7 elements to queue
for i in range(7):
    q.put(i)

# Check if queue is empty
q.empty() # False

# Remove items from front of queue 
# and print them.
while not q.empty():
    print(q.get())

# 0
# 1
# 2
# ...

# FIFO policy

q.empty() # True

# queues are thread safe
# different threads can add and remove from
# a queue

# Making a stack, using the LifoQueue
q = queue.LifoQueue()

for i in range(7):
    q.put(i)

while not q.empty():
    print(q.get())

# 6
# 5
# 4
# ...

q.empty() # True

# The LifoQueue is thread safe

# With the case of multiprocessing
import time

q = queue.PriorityQueue()

q.put(5)
q.put(4)
q.put(3)
q.put(2)

while not q.empty():
    print(q.get())

