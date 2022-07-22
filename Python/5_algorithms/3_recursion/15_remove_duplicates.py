def remove_duplicates(s):
    if len(s) == 1: return s 
    if s[0] == s[1]:
        return remove_duplicates(s[1:])
    else:
        return s[0] + remove_duplicates(s[1:]) 

s = "aaabbcccddaaa"
print( remove_duplicates(s) )

