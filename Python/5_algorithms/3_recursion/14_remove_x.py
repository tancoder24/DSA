def removeX(s):
    if len(s) == 0:
        return ""
    
    if s[0] == "x":
        return removeX(s[1:])
    else:
        return s[0] + removeX(s[1:])
    
s = "abxcdxefdxgf"
print( removeX(s) )