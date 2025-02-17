# Queue implementation using Array

class Queue:
    def __init__(self, capacity):
        self.arr = [0] * capacity
        self.capacity = capacity
        self.size = 0
        self.front = 0

    def isFull(self):
        if self.size == self.capacity:
            return True
        return False
    
    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def enqueue(self, data):
        if self.isFull():
            return "Stack overflow"
        
        self.arr[self.size] = data
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return 
        
        # Shift elements left
        for i in range(1, self.size):
            self.arr[i-1] = self.arr[i]
        self.size -= 1

    def getFront(self):
        if self.size == 0:
            return -1
        return self.arr[self.front]    

    def display(self):
        for i in range(self.front, self.size):
            print(self.arr[i], end=" ")  
        print()

obj = Queue(4)
print(obj.isFull())
obj.enqueue(9)
obj.enqueue(8)
obj.enqueue(9)
obj.enqueue(9)
obj.enqueue(9)
print(obj.enqueue(9))
obj.dequeue()
print(obj.isFull())
print(obj.getFront())   
obj.display() 