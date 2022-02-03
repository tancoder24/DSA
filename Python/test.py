from collections import Counter 

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    Nshop = list(map(int, input().split()))
    M = int(input())

    NshopCounter = Counter(Nshop)
    chocolates = list(NshopCounter.keys())
    revenue = 0
    
    for i in range(M):
        X, chocolate = list(map(int, input().split()))
        if chocolate not in chocolates:
            continue
        if NshopCounter[chocolate] != 0:
            revenue += X
            NshopCounter[chocolate] -= 1
    print(revenue)
    return 0

if __name__ == '__main__':
    main()

#     5
# 50 1
# 20 3
# 25 3
# 5 12
# 20 11