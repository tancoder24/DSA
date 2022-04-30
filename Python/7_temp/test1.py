def check_duplicy_newLang(S):
    return not len(S) == len(set(S))

def convertString(S, C):
    if check_duplicy_newLang(S):
        return "New language Error"

    arr = []
    temp = []
    new_word = ""

    for c in C:
        if c == " ":
            arr.append(temp)
            temp = []
            continue
        elif c not in S:
            continue
        temp.append(S.index(c))
    arr.append(temp)

    for ar in arr:
        ar.sort()
    
    for ar in arr:
        for a in ar:
            new_word += S[a]
        new_word += " "
        
    return new_word

if __name__ == "__main__":

    # New Lang Sequence
    S = "palskdjfieuryt93516247oh".lower()

    # word to be transferred
    C = "Philacodist 2021".lower()

    ans = convertString(S, C)

    print(ans, end="")