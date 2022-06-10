"""
This is for only learning purpose, how hash works behind schene
while programming we use dict
"""

# collision handled using linear programming

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for k in key:
            h += ord(k)
        return h % 10

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = [key, val]
            return

        i = h + 1
        while i < self.MAX:
            if self.arr[i] is None:
                self.arr[i] = [key, val]
                return
            i += 1
        
        i = 0
        while i < h:
            if self.arr[i] is None:
                self.arr[i] = [key, val]
                return
            i += 1

        return "Value can't be stored"

    def __getitem__(self, key):
        h = self.get_hash(key)

        if self.arr[h][0] == key:
            return self.arr[h][1]
        
        i = h + 1
        while i < self.MAX:
            if self.arr[i][0] == key:
                return self.arr[i][1]
            i += 1
        
        i = 0
        while i < h:
            if self.arr[i][0] == key:
                return self.arr[i][1]
            i += 1

        return "Value not Found"


if __name__ == "__main__":

    h = HashTable()
    h["6 march"] = 100
    h["7 marbh"] = 80
    h["3 march"] = 60
    h["4 march"] = 40

    print(h.arr)
