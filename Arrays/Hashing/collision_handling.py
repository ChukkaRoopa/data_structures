class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.max
    
    def add(self, key, value):
        h = self.get_hash(key)
        
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def get(self, key):
        h = self.get_hash(key)
        
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
            
    def delete(self, key):
        h = self.get_hash(key)

        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
   
obj = HashTable()

print(obj.get_hash('march 6'))
print(obj.get_hash('march 17'))

obj.add('march 6', 345)
obj.add('march 17', 456)
obj.add('march 17', 45)
obj.add('march 18', 4578)

print(obj.arr)

print(obj.get('march 6'))
print(obj.get('march 17'))

obj.delete('march 17')

print(obj.arr)
