arr = [5, 6, 5, 5, 6]

def all_index1(arr, n):
    if len(arr) == 0: return []

    ans = all_index1(arr[1:], n)

    for i in range(len(ans)):
        if ans[i] > -1: ans[i] += 1
    
    if arr[0] == n:
        ans.insert(0, 0)

    return ans

def all_index2(arr ,n):
    if len(arr) == 0: return []

    ans = all_index2(arr[:-1] , n)

    if arr[-1] == n:
        ans.append(len(arr)-1)
        
    return ans

print( all_index1(arr, 5) )
print( all_index2(arr, 5) )