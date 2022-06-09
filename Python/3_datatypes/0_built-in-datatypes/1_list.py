fruits = ["apple", "banana", "cherry"]

# to make a new list with same values, using = will refer to same list
fruits2 = fruits.copy()
fruits2 = list(fruits)

"""
fruits.sort()
fruits.sort(reverse=True)

def myfunc(n):
  return "a" in n
fruits.sort(key = func)

# To sort case insensitive, by default its case sesitive
fruits.sort( key = str.lower )
"""

# change values using list indexing and new list
fruits[0:2] = ["dog", "cat"]
print(fruits)

# 1 index and 2 new list item will shift item accordingly
fruits[0:1] = ["Car", "Bus"]
print(fruits)

# 2 index and 1 new list item will reduce size of list by 1
fruits[0:2] = ["Mobile"]
print(fruits)

fruits.clear()
print(fruits)

del fruits
print(fruits)