# stack using deque is advisable

from collections import deque

stack = deque()

stack.append("Earth")
stack.append("India")
stack.append("Delhi")
stack.append("Ashok Vihar")

stack.pop()
print( stack )

