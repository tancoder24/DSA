# pass - break
x = 6
while x != 0:
    print(x)
    if x == 6:
        pass
    else:
        print("break")
        break
    x -= 1