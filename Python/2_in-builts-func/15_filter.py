arr1 = [ 1,2,3,4,5,6 ]

def func(x):
    if x%2 == 0:
        return True
    else:
        return False

arr2 = list( filter( func, arr1 ) )

print(arr2)