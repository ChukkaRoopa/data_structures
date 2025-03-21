class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.max
    
    def add(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

obj = HashTable()

hash_index = obj.get_hash('march 6')
print(hash_index)

add_value = obj.add('march 6', 345)

get_value = obj.get('march 6')
print(get_value)