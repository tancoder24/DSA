#Return the factorial of the number N
def factorial(N):
    # Your code goes here
    output = 1

    if N == 0: return 0

    for i in range(1,N+1):
        output *= i

    return output

if __name__ == "__main__":
    inp = int(input())
    print( factorial( inp ) )