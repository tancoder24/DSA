def merge_sort(arr):

    # 1. base case when size of arr = 0
    l = len(arr)
    if l <= 1: return arr

    # 2. recurrsion call
    sorted_arr = []
    left = merge_sort( arr[:l//2] )
    right = merge_sort( arr[(l//2):] )

    # 3. some calculations
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1

    return sorted_arr 


if __name__ == "__main__":
    arr = [2,1,4,3,6,4,3,2]
    
    print(arr)
    print( merge_sort(arr) )