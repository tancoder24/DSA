import queue

# queue.LifoQueue( max size(default infinite and for 0 or -ve I) )
q = queue.LifoQueue()

q.put_nowait(1)
q.put_nowait(2)
q.put_nowait(3)

print(q.get_nowait())
print(q.get_nowait())
print(q.get_nowait())

print()
print(dir(q))