arr = [1,2,3,3,4,3]

def first_index1(arr, n):
    if len(arr) == 0: return -1
    if arr[0] == n: return 0
    if len(arr) == 1: return -1
    ans = first_index1(arr[1:], n)
    return -1 if ans == -1 else ans+1

def first_index2(arr, n):
    if len(arr) == 0: return -1

    ans = first_index2(arr[:-1], n)

    if ans == -1 and arr[-1] == n:
        return len(arr)-1

    return -1 if ans == -1 else ans

     

ans1 = first_index1(arr, 3)
ans2 = first_index2(arr, 3)

print(ans1)
print(ans2)