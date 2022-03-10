"""
Find index of all the occurances of a number from sorted list

numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_to_find = 15  
This should return 5,6,7 as indices containing number 15 in the array
"""

def binary_search_occurence(arr, val):
    left_index = 0
    right_index = len(arr) - 1
    mid_index = 0
    val_occur = []

    while (left_index <= right_index):
        mid_index = (left_index + right_index) // 2
        mid_element = arr[mid_index]

        if mid_element == val :
            val_index = mid_index

            while arr[val_index] == val:
                val_index -= 1
            
            val_index += 1

            while arr[val_index] == val:
                val_occur.append(val_index)
                val_index += 1

            return val_occur

        elif mid_element > val:
            right_index = mid_index - 1

        elif mid_element < val:
            left_index = mid_index + 1

    return - 1

if __name__ == "__main__":
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    
    ans =  binary_search_occurence(numbers, 1) 

    print(ans)