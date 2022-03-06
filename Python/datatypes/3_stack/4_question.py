from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def is_empty(self):
        if len(self.container) < 1: return True
        return False

def reverseString(string):
    stack = Stack() 

    for s in string:
        stack.push(s)

    string = ""

    while (not stack.is_empty()):
        string += stack.pop()

    return string

def parenthesisChecker(string):
    stack = Stack() 
    
    isMatch = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }
    
    for s in string:
        if s == "[" or s == "{" or s == "(":
            stack.push(s)
        elif s == "]" or s == "}" or s == ")":
            if not stack.is_empty():
                if isMatch[s] != stack.pop(): 
                    return False
            else: 
                return False
    
    return stack.is_empty()

if __name__ == "__main__":
    print( reverseString("Tanmay Gupta") )
    print( parenthesisChecker( "[a+b]*(x+2y)*{gg+kk}" ))