from collections import deque

myqueue = deque()

myqueue.appendleft("A")
myqueue.appendleft("B")
myqueue.appendleft("C")

myqueue.extendleft([1,23,4])

print( myqueue.pop() )
print( myqueue[0] )

# OR

q = deque()
  
# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')
  
print("Initial queue")
print(q)
  
# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
  
print("\nQueue after removing elements")
print(q)
