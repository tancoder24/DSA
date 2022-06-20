class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def __str__(self):
        temp = self.front
        data = ""
        while temp:
            data += str(temp.data) + " "
            temp = temp.next
        return data

    def enqueue(self, data):
        if self.isEmpty():
            node = Node(data)
            self.front = node
            self.rear = node
            return
        self.rear.next = Node(data)
        self.rear = self.rear.next

    def dequeue(self):
        if self.isEmpty():
            return "IS EMPTY"
        data = self.front.data
        self.front = self.front.next
        return data

if __name__ == "__main__":

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue)

    print( queue.dequeue() )
    print( queue.dequeue() )
    print( queue.dequeue() )
    print( queue.dequeue() )
    print( queue.dequeue() )


