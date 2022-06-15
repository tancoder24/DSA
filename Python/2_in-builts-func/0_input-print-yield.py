from pydoc import isdata


x = input("please type")
a = "Tanmay"

# to print output in a line
for i in a: 
    print(i, end="")

# sep is used for saperation of words default is ''
print("Tanmay", "Gupta", 20, sep="#")

# yield mostly not used
def nextSquare():
    i = 1
    while True:
        yield i*i                
        i += 1 # Next execution resumes
                # from this point    
# Driver code
for num in nextSquare():
    if num > 100:
        break   
    print(num)