"""
This is for only learning purpose, how hash works behind schene
while programming we use dict
"""

# collision handled using chaining

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
        h = 0
        for k in key:
            h += ord(k)
        return h % 100

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        for arr in self.arr[h]:
            if arr[0] == key:
                arr[1] = val
                return
        self.arr[h].append([key, val])

    def __getitem__(self, key):
        h = self.get_hash(key)
        for arr in self.arr[h]:
            if arr[0] == key:
                return arr[1]

    def __delitem__(self, key):
        h = self.get_hash(key)

        for i in range( len( self.arr[h] )):
            if self.arr[h][i][0] == key:
                self.arr[h].pop(i)
                return

if __name__ == "__main__":
    
    h = HashTable()
    h["1 march"] = 100
    h["2 march"] = 80
    h["3 marbh"] = 60
    h["3 march"] = 40
    h["3 march"] = 400
    
    del h["1 marbh"]

    print( h["1 march"])
    print( h["2 march"])
    print( h["3 marbh"])
    print( h.arr)

