def temp(x):
    if len(x) == 1:
        return
    x[0] += 1
    temp(x[1:])

x = [1,2,3,4]

temp(x)
print(x)
            