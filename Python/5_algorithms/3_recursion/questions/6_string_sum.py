# 1st way
def string_sum(num):
    num = str(num)
    if len(num) == 1:
        return int(num[0])
    
    return int(num[0]) + string_sum(num[1:])

# 2nd way

def string_sum(num):
    if num == 0:
        return 0
    
    return (num % 10) + string_sum(num//10)

if __name__ == "__main__":
    ans = string_sum(123)

    print(ans)