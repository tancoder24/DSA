x = input("please type")

# to reverse a list, tupple, string
a = [1,2,3,4]
print(a[::-1])

b = (5,6,7,8)
b = list(reversed(b))
print( b )

c = "tanmay"
print(c[::-1])

# to print output in a line

for i in a: 
    print(i, end="")

for i in a: 
    print(i, end="$")

print()
print("Tanmay", "Gupta", 20, sep="#")