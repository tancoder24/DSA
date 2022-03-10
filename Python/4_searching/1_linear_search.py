def linear_search(arr, val):
    for index, element in enumerate(arr):
        if element == val:
            return index
    return -1

if __name__ == "__main__":
    
    arr = [2,4,6,8,10]
    
    ans = linear_search(arr, 60)
    print(ans)