from collections import deque

myqueue = deque()

myqueue.appendleft("A")
myqueue.appendleft("B")
myqueue.appendleft("C")

myqueue.extendleft([1,23,4])

print( myqueue.pop() )
print( myqueue[0] )