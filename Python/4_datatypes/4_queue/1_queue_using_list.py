# insert at 0 and pop at -1
letters = []
letters.insert(0, "A")
letters.insert(0, "B")
letters.insert(0, "C")
letters.insert(0, "D")
letters.insert(0, "E")
letters.insert(0, "F")

print(letters)
print( letters.pop() )
print( letters.pop() )
print( letters.pop() )

# insert at -1 and pop at 0
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)
numbers.append(6)

print(numbers)
print( numbers.pop(0) )
print( numbers.pop(0) )
print( numbers.pop(0) )
print( numbers.pop(0) )