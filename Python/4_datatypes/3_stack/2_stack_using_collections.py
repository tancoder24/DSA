# stack using deque is advisable

from collections import deque

stack = deque()

# push
stack.append("Earth")
stack.append("India")
stack.append("Delhi")
stack.append("Ashok Vihar")

# pop
stack.pop()

# peak
print("peak ->", stack[-1] )

# length
print(f"length -> {len(stack)}")

print( stack )

print()
print(dir( stack ))
