from collections import deque

class Queue:
    def __init__ (self):
        self.myqueue = deque()
    
    def enqueue(self, value):
        self.myqueue.appendleft(value)

    def dequeue(self):
        return self.myqueue.pop()

    def is_empty(self):
        return self.size() < 1

    def size(self):
        return len(self.myqueue)

names = Queue()

names.enqueue({
    "fname": "Tanmay",
    "lname": "Gupta"
})
names.enqueue({
    "fname": "Hare",
    "lname": "Krishna"
})
names.enqueue({
    "fname": "Shiv",
    "lname": "Shankar"
})

print( names.myqueue )

print(names.dequeue())
print(names.dequeue())
print(names.dequeue())