def reverse_func(s):
    s[:] = s[::-1]
    return s

if __name__ == "__main__":

    s = list("Tanmay Gupta")
    
    # user defined func
    s = reverse_func(s)
    print( "".join( s ))
    
    # in-built func
    s.reverse()
    print("".join( s ))