class CircularQueue:
    def __init__(self, size):
        self.Q = [None]*size
        self.head = self.rear = -1
        self.MaxSize = size

    def isEmpty(self):
        if self.head == -1:
            return True

    def isFull(self):
        if self.head == 0 and self.rear == self.MaxSize-1:
            return True
        elif self.head - 1 == self.rear:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.isFull():
            print("Stack Full")
        if self.rear == -1:
            self.head = self.rear = 0
            self.Q[self.rear] = data

        elif self.rear < self.MaxSize-1:
            self.rear += 1
            self.Q[self.rear] = data

        elif self.head > 0 and self.rear == self.MaxSize-1:
            self.rear = 0
            self.Q[self.rear] = data

    def dequeue(self):
        if self.isEmpty():
            return "Stack Empty"
        
        if self.head == self.rear:
            data = self.Q[self.head]
            self.Q[self.head] = None
            self.head = self.rear = -1
            
        elif self.head == self.MaxSize - 1:
            data = self.Q[self.head]
            self.Q[self.head] = None
            self.head = 0

        else:
            data = self.Q[self.head]
            self.Q[self.head] = None
            self.head += 1 

        return data

if __name__ == "__main__":
    queue = CircularQueue(5)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    

    print( queue.dequeue() )
    queue.enqueue(6)

    print( queue.dequeue() )
    queue.enqueue(7)

    print(queue.Q)

