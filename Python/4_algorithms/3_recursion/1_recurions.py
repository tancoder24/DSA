def find_sum(n):
    total_sum = 0
    for i in range(1,n+1):
        total_sum += i
    return total_sum

def find_sum_recursive(n):
    if n==1:
        return 1
    return n + find_sum_recursive(n-1)
    

if __name__ == "__main__":

    ans1 = find_sum(5)
    print(ans1)

    ans2 = find_sum_recursive(5)
    print(ans2)