arr = ["apple", "banana", "orange"]

x = iter(arr)
print(x)
print(next(x))
print(next(x))
print(next(x))

###########################################

class myClass:
    def __iter__(self):
        self.a = 1        
        return self

    def __next__(self):
        if self.a > 3:
            raise StopIteration
        ans = self.a
        self.a += 1
        return ans

a = myClass()
b = iter(a)

for x in b:
  print(x)


print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))