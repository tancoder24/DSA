"""
    datatypes
    1. int
    2. float
    3. complex
    4. string
    5. boolean
    7. list
    8. tupple
    9. range
    10. dict
    11. set
"""

# variable declaration 
a = 5
b = 6

# function declaration
def sum(a,b):
    print(a+b)

sum(a,b)

# conditional operators 
if True:
    print(str(True) + " if-else")
elif False:
    print(False)
else :
    print("Nothing")

# array
arr = [1,2,3]
print(len(arr))

# loops ( only 2 types in py )
i = 0
while(i<1):
    print("while-else")
    i = 1
else:
    print("else-while")

for i in range(1):
    print("for-else")
else:
    print("else-for")
