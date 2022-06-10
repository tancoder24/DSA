# Write a Python program to calculate the sum of a list of numbers. 

# 1st way
def sum_arr(arr, start, end):
    while start < end:
        total = arr[start] + sum_arr(arr, start+1, end)
        return total
    else:
        return arr[end]

# 2nd way
def sum_arr(arr):
    if len(arr) == 1:
        return arr[0]
    
    return arr[1] + sum_arr(arr[1:])


if __name__ == "__main__":
    
    arr = [30,41,52,61,72]

    ans = sum_arr(arr)

    print(ans)