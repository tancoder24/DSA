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

    def add(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

if __name__ == "__main__":
    
    t = HashTable()
    t.add("6 march", 100)
    ans = t.get("6 march")
    
    print(ans)
    