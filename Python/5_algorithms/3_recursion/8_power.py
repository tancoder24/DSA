def power(a, b):
    if b <= 1:
        return a
    return a * power(a, b-1)

if __name__ == "__main__":
    
    ans = power(3,4)

    print(ans)