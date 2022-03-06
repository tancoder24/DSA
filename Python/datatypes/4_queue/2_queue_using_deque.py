from collections import deque

myqueue = deque()

myqueue.appendleft("A")
myqueue.appendleft("B")
myqueue.appendleft("C")

print( myqueue.pop() )
print( myqueue.pop() )