"""
newlist = [expression for item in iterable if condition == True]
                
                OR
newlist = [x.upper() for x in fruits]
newlist = [x.upper() for x in fruits if "a" in x]
newlist = [x.upper() if x=="orange" else x.lower() for x in fruits if "a" in x]
"""

arr1 = [i**2 for i in range(10)]
print(arr1)

arr2 = ["HELLO" for i in range(10)]
print(arr2)