from collections import deque

# Turning List to queue
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

# Removing First Item
queue.popleft()
# Removing Last Item: Technically not a Queue Operation
queue.pop()

print(queue)

# Check if Queue is Empty
if not queue:
    print("empty")
