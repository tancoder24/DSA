# worst way
def swap1(x, y):
    temp = x
    x = y
    y = temp
    return x,y

# only in python
def swap2(x, y):
    x,y = y,x
    return x, y

# in all languages
def swap3(x, y):
    x = x + y
    y = x - y
    x = x - y
    return x, y

print( swap1(5, 10) )
print( swap2(5, 10) )
print( swap3(5, 10) )