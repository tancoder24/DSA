from collections import deque

class Myqueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.appendleft(value)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size < 1

    def front(self):
        return self.queue[-1]

    def print_binary(self, n):
        arr = []
        self.enqueue("1")

        while ( len(arr) < n):
            temp = self.dequeue()
            arr.append(temp)
            self.enqueue(temp+"0")
            self.enqueue(temp+"1")

        for a in arr:
            print(a)

if __name__ == "__main__":

    myqueue = Myqueue()

    myqueue.print_binary(10)