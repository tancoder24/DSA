import queue

# stack = queue.LifoQueue( max size(default infinite and for 0 or -ve I) )
stack = queue.LifoQueue()

# push
stack.put("Earth")
stack.put("India")
stack.put("Delhi")
stack.put("Ashok Vihar")

# pop
print( stack.get() )

print()
print(dir( stack ))