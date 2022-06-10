# immutable ordered

x = (1,2,3)

# only way to add value to tupple  or join tupples using +
x += (4,)
# or (convert to list and back to tupple)
x = list(x)
x.append(45)
x = tuple(x)
print(x)

z = x*2
print(f"z is {z}")

########################
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

green, yellow, *red = fruits
green, *red, yellow = fruits

print(green)
print(yellow)
print(red)
