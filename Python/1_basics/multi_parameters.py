# * operaor allows multiple values

def func(*a):
    print( type(a) ,"sum =", sum(a))

if __name__ == "__main__":

    func(1,2,3,4)


