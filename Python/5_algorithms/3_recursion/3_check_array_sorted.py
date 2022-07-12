arr = [1,2,3,4,5]

def sorted1(arr):
    if len(arr) == 1 or len(arr) == 0: return True
    if arr[0] < arr[1]:
        return sorted(arr[1:])
    else: 
        return False

def sorted2(arr):
    if len(arr) == 1 or len(arr) == 1:
        return True

    if sorted2(arr[1:]):
        return arr[0] < arr[1]
    else: 
        return False

ans = sorted2(arr)
print(ans)