# priority queue is implemented using HEAP
# in python we use heapq which only provides min heap

import heapq

# initalize list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)
print(f"created heap is -> {li}")
print()

# using heappush() to push elements 4 into heap
heapq.heappush(li, 4)
print(f"heap after 4 pushed -> {li}")
print()

# heappop to pop min element
x = heapq.heappop(li)
print(f"min element -> {x}")
print()

# using heappushpop() to push and pop items simultaneously
# 1st push and mantain heap than pop 
x = heapq.heappushpop(li, 0)
print(f"min ele -> {x}")
print(f"new heap -> {li}")
print()

# heapreplace() pops first than add new element and maintain heap
x = heapq.heapreplace(li, 0)
print(f"min ele -> {x}")
print(f"new heap -> {li}")
print()

# using nlargest to print n largest numbers
print("The 3 largest numbers in list are : ",end="")
print(heapq.nlargest(3, li))
# using nsmallest to print n smallest numbers
print("The 3 smallest numbers in list are : ",end="")
print(heapq.nsmallest(3, li))
print()