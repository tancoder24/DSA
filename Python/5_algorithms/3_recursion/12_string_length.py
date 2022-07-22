def length(s):
    if len(s) == 0: return 0
    return length(s[1:]) + 1 

name = "Tanmay Gupta"
print( length(name) )