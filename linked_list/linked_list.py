# Create a node class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None     # reference is none bcz if we have only one node then there is nothing in its reference

class LinkedList:
    def __init__(self):
        self.head = None
        
    # Insertion in the linked list

    # Insert at beginning in the linked list
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Insert the node at specific position in linked list
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)

        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position = position + 1
            current_node = current_node.next
        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # Insert the node at the end
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    # Update the node of a Linked list
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val

        else:
            while (current_node != None and position != index):
                position = position + 1
                current_node = current_node.next
            if current_node != None:
                current_node.data = val
            else:
                print("Index not found.")

    # Delete node in a linked list

    # Remove first node from the linked list
    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    # Remove the last node from  the linked list
    def remove_last_node(self):
        if self.head is None:
            return
        
        current_node = self.head
        while (current_node.next != None and current_node.next.next != None):
            current_node = current_node.next
        current_node.next = None 

    # Delete a linked list node at a given position
    def remove_at_index(self, index):
        if self.head is None:
            return

        current_node = self.head
        position = 0
        if (position == index):
            self.remove_first_node() 
        else:
            while (current_node != None and position+1 != index):
                position = position + 1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")      

    # Delete a linked list node of given data
    def remove_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return
        
        while (current_node != None and current_node.next.data != data):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next == current_node.next.next

    # Linked list traversal
    def printLL(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next

    # Get the length of the linked list
    def sizeOfLL(self):
        size = 0
        if (self.head):
            current_node = self.head
            while(current_node):
                size += 1
                current_node = current_node.next
            return size
        else:
            return 0
        
# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

# print the linked list
print("Node Data")
llist.printLL()

# remove a nodes from the linked list
print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()
print("Remove Node at Index 1")
llist.remove_at_index(1)

# print the linked list again
print("\nLinked list after removing a node:")
llist.printLL()

print("\nUpdate node Value")
llist.updateNode('10', 0)
llist.printLL()

print("\nSize of linked list :", end=" ")
print(llist.sizeOfLL())