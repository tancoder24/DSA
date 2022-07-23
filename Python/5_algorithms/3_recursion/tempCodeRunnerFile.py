def subsequence(s):
    if len(s) == 1:
        return ["", s[0]]
    
    arr = subsequence(s[1:])

    for a in arr:
        arr.append(s[0]+a)

    return arr

if __name__ == "__main__":
    s = "ab"
    arr = subsequence(s)

    print(s)
    print(arr)