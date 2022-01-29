# in dict checks only for keys not values
dictionary = {
    True: False,
    1: "1",
    23: 32
}
print( all(dictionary) )


S = [1,2,3,4,5]

"""
any
Returns True if any item in an iterable object is true
"""
output1 = any(i % 2 == 0 for i in S)
print(output1)

"""
all
Returns True if all item in an iterable object is true
"""
output2 = all(i % 2 == 0 for i in S)
print(output2)

    


