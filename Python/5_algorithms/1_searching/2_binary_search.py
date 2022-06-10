def binary_search(arr, val):
    left_index = 0
    right_index = len(arr)-1
    mid_index = 0

    while ( left_index <= right_index ):
        mid_index = (left_index + right_index) // 2
        mid_value = arr[mid_index]

        if mid_value == val:
            return mid_index
        
        elif mid_value > val:
            right_index = mid_index - 1

        elif mid_value < val:
            left_index = mid_index + 1 
    
    return -1

def binary_search_recursive(arr, val, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_value = arr[mid_index]

    if mid_value == val:
        return mid_index
    
    elif mid_value < val:
        left_index = mid_index + 1

    elif mid_value > val:
        right_index = mid_index - 1

    return binary_search_recursive(arr, val, left_index, right_index)

if __name__ == "__main__":
    arr = [12, 15, 17,  19, 21, 24, 45, 67]

    ans = binary_search(arr, 100)
    print(ans)

    rec_ans = binary_search_recursive(arr, 67, 0, len(arr)-1)
    print(rec_ans)