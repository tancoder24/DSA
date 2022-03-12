"""
The zip() function returns a zip object, which is an iterator of tuples where 
the first item in each passed iterator is paired together, and then the second 
item in each passed iterator are paired together etc.

If the passed iterators have different lengths, the iterator with the least 
items decides the length of the new iterator.

"""

tuple1 = (1,3,5,7,9)
tuple2 = (2,4,6,8)

output = zip(tuple1,tuple2)

# tuple function is used to make returned object readable
print( tuple(output) )