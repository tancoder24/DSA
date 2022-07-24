def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quick_sort(elements, start, end):

    # 1. base case 
    if start >= end :
        return 

    # 2. Calculations
    pivot = elements[start]
    smaller =  0
    
    for element in elements[start: end+1]:
        if element < pivot:
            smaller += 1
    swap(elements, start+smaller, start)

    i = start
    j = end
    while i < j:
        if elements[i] < pivot and elements[j] > pivot:
            i += 1
            j -= 1
        elif elements[i] > pivot and elements[j] < pivot:
            swap(elements, i, j)
            i += 1
            j -= 1
        elif elements[i] > pivot:
            j -= 1
        else:
            i += 1    

    # 3. recurrsive calls
    quick_sort(elements, start, start+smaller-1)
    quick_sort(elements, start+smaller+1, end)

if __name__ == "__main__":
    arr1 = [11, 9, 29, 7, 2, 15, 28]
    print(arr1)
    quick_sort(arr1, 0, 6) 
    print(arr1)

    print()

    arr2 = [11, 9, 29, 7, 2, 15, 28, -1]
    print(arr2)
    quick_sort(arr2, 0, 7)
    print(arr2) 