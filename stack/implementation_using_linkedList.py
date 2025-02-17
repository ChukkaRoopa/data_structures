# Stack implementation using linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack_using_linkedlist:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        return False
        
    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            self.head = self.head.next

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.head.data 
  
obj = stack_using_linkedlist()

print(obj.isEmpty())
obj.push('r')
obj.push('s')
obj.push('m')
obj.pop()
print(obj.isEmpty())
print(obj.peek())