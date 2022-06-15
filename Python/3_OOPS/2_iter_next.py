# print countdown

class Parent:
    def __init__(self, val):
        self.val = val

    def __iter__(self):
        return self

    def __next__(self):
        if self.val < 1:
            raise StopIteration
        self.val -= 1
        return self.val

p = Parent(6)

p_iter = iter(p)

print( next(p_iter) )
print( next(p_iter) )
print( next(p_iter) )
print( next(p_iter) )
print( next(p_iter) )
print( next(p_iter) )
print( next(p_iter) )