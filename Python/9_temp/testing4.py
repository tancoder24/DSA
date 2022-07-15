def sort012(arr,n):
    # code here
    zero = 0
    one = 0
    two = n-1
        
    while one < two:
        if arr[one] == 2:
            arr[one], arr[two] = arr[two], arr[one]
            two -= 1
        elif arr[one] == 0:
            arr[one], arr[zero] = arr[zero], arr[one]
            one += 1
            zero += 1
        elif arr[one] == 1:
            one += 1
    return arr

arr = [0,1,0]

ans = sort012(arr,3)
