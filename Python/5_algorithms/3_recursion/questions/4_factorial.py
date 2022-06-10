def factor(n):
    if n == 1:
        return 1
    return n * factor(n-1)

if __name__ == "__main__":
    ans = factor(5)

    print(ans)