import itertools 

arr = [1,23,3]

def func(value1, value2):
  return value1*value2

print( list(itertools.accumulate(arr, func)) )