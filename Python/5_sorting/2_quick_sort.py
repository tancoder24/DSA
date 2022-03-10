# def hoare_quick_sort(arr):
#     pivot = 0
#     start = 1
#     end = len(arr) - 1

#     while(start < len(arr)):
#         if arr[start] > arr[pivot]:
#             while(end >= start):
#                 if arr[end] < arr[pivot]:
#                     arr[start], arr[end] = arr[end], arr[start] 
#                     break
#                 end -= 1
#             else: 
#                 arr[end], arr[pivot] = arr[pivot], arr[end]
#                 leftArr = hoare_quick_sort(arr[0: end])
#                 rightArr = hoare_quick_sort(arr[end+1:])
#                 arr = leftArr + [arr[end]] + rightArr
#                 return arr
#         start += 1

def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

def partition(elements):
    pivot_index = 0
    pivot = elements[pivot_index]

    start = pivot_index + 1
    end = len(elements) - 1

    while start < end:
        while ( elements[start] <= pivot ):
            start += 1

        while ( elements[end] > pivot ):
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

def quick_sort(elements):
    partition(elements)

if __name__ == "__main__":
    arr = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(arr) 
    print(arr)