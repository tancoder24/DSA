"""
    datatypes
    
    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type:	NoneType
    
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

# int
a = int(-5)
a = 5
print( type(a) )

# float
b = float(6.0)
b = 6.0
b = 6e5             # e to show power of 10
print( type(b) )

# complex
c = complex(4 + 2j)
c = 4 + 2j          # j to show imaginary part 
print( type(c) )

# string
d = str("tanmay")
d = "tanmay"
e = "g"
print( type(d), " ", type(e))

# boolean
f = bool(True)
f = True
print( type(f) )

# list
g = list((1,2,3))
g = [1,2,3]
print( type(g) )

# tupple
h = tuple((1,2,3))
h = (1,2,3) 
h = 1,2,3
print( type(h) )

# To declare 1 element tuple use , and () is not necessary for tuple
h2 = (1,)
h2 =  2,
print(type(h2), h2)

# range
i = range(3) 
print( type(i) )

# dict
j = dict(fname="tanmay", lname="gupta")
j = {
    True: False,
    False: "1",
    23: 32
}

print( type(j), j[23] )

# set
k = set(("a", "b"))
k = {"a"}
print( type(k) )