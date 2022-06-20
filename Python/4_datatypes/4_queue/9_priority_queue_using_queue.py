import queue

pq = queue.PriorityQueue()

pq.put_nowait(10)
pq.put_nowait(5)
pq.put_nowait(20)
pq.put_nowait(15)

print( pq.get_nowait() )
print( pq.get_nowait() )
print( pq.get_nowait() )
print( pq.get_nowait() )

