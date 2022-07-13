arr = [1,2,3,1,2,3,1,2,3]

def last_index1(arr, n):
    if len(arr) == 0: return -1

    if arr[-1] == n: return len(arr)-1
    
    if len(arr) == 1: return -1
    
    return last_index1(arr[:-1], n)

def last_index2(arr,n):
    if len(arr) == 0: return -1
    ans = last_index2(arr[1:], n)

    if ans == -1 and arr[0] == n:
        return 0

    return -1 if ans == -1 else ans + 1

ans1 = last_index1(arr, 2)
ans2 = last_index2(arr, 2)

print(ans1)
print(ans2)