def print_keypad(n, keypad, output=""):
    
    # 1. base case
    if len(n) < 1:
        print(output)
        return

    # 2. recurrsive call
    for c in keypad[ int(n[0])-1 ]:
        print_keypad(n[1:] , keypad, output+c)

if __name__ == "__main__":
    n = "23"
    keypad = ["", "ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"]

    print_keypad(n, keypad)