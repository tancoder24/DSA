def subsequence(s):
    # 1. base case where recurrsion stops
    if len(s) == 1:
        return ["", s[0]]
    
    # 2. recurrsion calls
    arr = subsequence(s[1:])

    # 3. some calculations
    arr += [s[0]+a for a in arr]
    return arr

if __name__ == "__main__":
    s = "abc"
    arr = subsequence(s)

    print(s)
    print(arr)