x = "                 my name is          tanmay             "

a = x.strip()
print(a)

b = a.split()
print(b)

c = "%".join(b)
print(c)

##################################################################
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])
print(a[0:8:3])


