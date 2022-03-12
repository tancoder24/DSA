"""
This is for only learning purpose, how hash works behind schene
while programming we use dict
"""

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for k in key:
            h += ord(k)
        return h % 100 

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

if __name__ == "__main__":
    
    t = HashTable()
    t["6 march"] = 100
    t["7 march"] = 200

    print( t["6 march"] )
    print( t["7 march"] )
    
    del t["6 march"] 

    print( t["6 march"] )