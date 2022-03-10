def print_fibonacci(n):
    a = 0
    b = 1
    total = 0
    ans = ""
    for i in range(n):
        ans += str(a) + " "
        total = a + b
        a = b
        b = total
    return ans

def rec_fibonacci(n):
    if n == 1 or n == 0:
        return n
    return  rec_fibonacci(n-1) + rec_fibonacci(n-2)

if __name__ == "__main__":
    
    print(print_fibonacci(5)) 
    print( rec_fibonacci(5) )