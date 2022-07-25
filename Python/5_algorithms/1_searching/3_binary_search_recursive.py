def bin_search(n, arr, i, j):

    # 1. base case
    l = j-i+1
    mid = (l//2)+i
    if l == 0:
        print("VAL NOT FOUND")
        return         
    
    # 2. calculations
    if arr[mid] == n:
        print(mid)
        return
    elif l == 1:
        print("VAL NOT FOUND")
        return 
    elif arr[mid] > n:
        j = mid-1
    elif arr[(mid)] < n:
        i = mid+1

    # 3. reccursive call
    bin_search(n, arr, i, j)


    return

if __name__ == "__main__":
    arr = [100, 11, 9, 29, 7, 5, 2, 15, 28]
    arr.sort()
    bin_search(100, arr, 0 , 8) 