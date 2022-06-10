# stack using a list is not advisble

# stack using list
address = []

# to push new element
address.append("Earth")
address.append("India")
address.append("Delhi")
address.append("Ashok Vihar")

# size
print( f"size of stack {len(address)}" )

# to peek last element
print("peak ", address[-1] )
print(address)

# to pop last elemnt
print("pop ", address.pop() )
print(address)