class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.stack = None
    
    def __str__(self):
        temp = self.stack
        data = ""
        while temp:
            data += str(temp.data) + " "
            temp = temp.next
        return data

    def isEmpty(self):
        if self.stack == None:
            return True
        else: 
            return False

    def push(self, data):
        if self.isEmpty():
            self.stack = Node(data)
            return
        node = Node(data)
        node.next = self.stack
        self.stack = node

    def pop(self):
        if self.isEmpty():
            return "Stack Empty"
        data = self.stack.data
        self.stack = self.stack.next
        return data

    def peek(self):
        if self.isEmpty():
            return "Stack Empty"
        return self.stack.data
        
if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack.peek())

    print(stack.pop())

    print(stack)

    print(stack.isEmpty())
    