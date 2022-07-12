arr = [1,2,13,4,5]

def sorted(arr):
    if len(arr) == 1: return True
    if arr[0] < arr[1]:
        return sorted(arr[1:])
    else: 
        return False

ans = sorted(arr)
print(ans)