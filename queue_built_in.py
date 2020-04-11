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

