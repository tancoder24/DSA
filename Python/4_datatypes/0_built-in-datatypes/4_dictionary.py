# key of the dictionary is always immutable whereas value can be both mutable and immutable
# immutable in python - Integers Float Booleans Strings Tuples
# mutable in python - Lists Dictionaries Sets

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# to copy 
mydict = thisdict.copy()
mydict = dict(thisdict)

# to acces dict items
x = thisdict["model"]
x = thisdict.get("model")

# Nested Dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}