# Queue implementation using linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        if self.front is None and self.rear is None:
            return True
        return False
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Stack is Empty")
            return
        
        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

    def getFront(self):
        if self.front is None:
            print("Stack is Empty")
            return -1
        return self.front.data
    
    def getRear(self):
        if self.rear is None:
            print("stack is empty")
            return
        return self.rear.data

        
obj = Queue()
obj.enqueue(4)
print(obj.isEmpty())
obj.enqueue(3)
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.enqueue(3)
obj.enqueue(6)
obj.dequeue()
print(obj.getFront())
print(obj.getRear())