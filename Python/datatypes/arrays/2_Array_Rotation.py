"""
worst way to do rotation 
"""

def rotateArrayUsingTemp(arr, n, d):
    d = d % n
    temp = arr[:d]
    arr = arr[d:]
    arr.extend(temp)
    return arr

if __name__ == "__main__":
    arr = [1,2,3,4]

    print( rotateArrayUsingTemp(arr, 4, 10) )