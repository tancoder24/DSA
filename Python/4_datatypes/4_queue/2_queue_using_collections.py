from collections import deque
###############################################################################
# append left and pop right
myqueue = deque()

myqueue.appendleft("A")
myqueue.appendleft("B")
myqueue.appendleft("C")

myqueue.extendleft([1,23,4])

print( myqueue.pop() )
print( myqueue[0] )

###############################################################################
# append right and pop left
q = deque() 

q.append('a')
q.append('b')
q.append('c')

print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
