# Implementation of stack using Array

class stack_using_array:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
        print(element + " is pushed into stack.")
        return self.stack

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False
        
    def pop(self):
        if (self.isEmpty()):
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if (self.isEmpty()):
            return "Stack is Empty"
        return self.stack[len(self.stack) - 1]
    

obj = stack_using_array()

obj.push(str(20))
obj.push(str(30))
print(obj.pop())
print(obj.isEmpty())
print(obj.peek())