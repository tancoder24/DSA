"""
Arbitrary Arguments, *args
function will receive a tuple of arguments
"""
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

########################################
"""
Arbitrary Keyword Arguments, **kwargs
function will receive a dictionary of arguments
"""
def my_func(**kid):
    print( kid["lname"] )
    print(kid)

my_func(fname="Tanmay", lname="Gupta" )

#########################################
"""
lambda function is a small anonymous function
lambda arguments : expression
"""
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# ex2
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))