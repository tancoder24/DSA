def possible_word(n, keypad):
    # 1. base case
    if len(n) == 1:
        return list(keypad[int(n) - 1])
    
    # 2. recurrsive call
    arr = possible_word(n[1:], keypad)
    
    # 3. some calculations
    res_arr = []
    for c in keypad[int(n[0]) - 1]:
        for ar in arr:
            res_arr.append(c+ar)
    return res_arr

if __name__ == "__main__":
    keypad = ["", "ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"]

    n = "234"
    ans = possible_word(n, keypad)
    print(ans)