# pass - break
# pass is just to avoid error when we dont have any code to execute
# like below at x == 6 

x = 6
while x > 0:
    print(x)

    if x == 6:
        print("before pass")
        pass
        print("after pass")

    elif x == 3:
        print("before continue")
        x -= 1
        continue
        print("after continue")

    elif x < 3 :
        print("break")
        break
    x -= 1