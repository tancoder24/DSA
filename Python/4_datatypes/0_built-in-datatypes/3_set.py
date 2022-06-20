# set can have only immutable objects as elemnets
# immutable in python - Integers Float Booleans Strings Tuples
# mutable in python - Lists Dictionaries Sets

# basics
set1 = {1,2,3}

set2 = set1         # set2 is just refering to set1
set2.remove(1)

set2 = set1.copy() 
set2 = set(set1)

set2.clear()

print(set1)

# union of both set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set1, set2, set3)

set1.update(set2)
print(set1, set2, set3)

##################################################################
# keep only duplicate
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(x, z)

x.intersection_update(y)
print(x)

################################################################3
# keep all itmes except duplicate
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z)

x.symmetric_difference_update(y)
print(x)

"""

isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not

"""