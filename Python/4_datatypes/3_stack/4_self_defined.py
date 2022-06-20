from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def peek(self):
        return self.container[-1]

    def length(self):
        return len(self.container)

    def pop(self):
        return self.container.pop()

    def is_empty(self):
        return self.length() == 0

if __name__ == "__main__":
    
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack.peek())
    print(stack.pop())
    print(stack.length())
    print(stack.is_empty())