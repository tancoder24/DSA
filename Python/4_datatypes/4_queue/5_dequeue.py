from collections import deque

queue = deque( ["A", "B", "C"] )

print(queue)

# to append on right
queue.append("E")
# to append on left
queue.appendleft("0")

print(queue)

# to remove left
queue.pop()
# to remove right
queue.popleft()

print(queue)