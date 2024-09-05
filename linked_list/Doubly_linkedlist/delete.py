# Deletion of DLL

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

# Deletion at the beginning
def delete_at_beginning(head):
    if head is None:
        print("DLL is empty")
        return None
    
    if head.next is None:
        return None
    
    new_node = head.next
    new_node.prev = None
    del head
    return new_node

# Delete at a given index
def delete_at_given_position(head, index):
    if head is None:
        print("DLL is empty")
        return
    
    if index < 0:
        print("Invalid index")
        return head
    
    if index == 0:
        if head.next:
            head.next.prev = None
        return head.next
    
    current_node = head
    position = 0
    while (current_node!= None and position+1 != index):
        current_node = current_node.next
        position += 1
    
    if current_node != None:
        if current_node.next:
            current_node.next.prev = current_node.prev
        if current_node.prev:
            current_node.prev.next = current_node.next
        del current_node
        return head
    else:
        print("Index out of range")
        return head

# Delete at the end
def delete_at_end(head):
    if head is None:
        print("DLL is empty")
        return
    if head.next is None:
        return None
   
    current_node = head
    while current_node.next.next:
        current_node = current_node.next
    del_node = current_node.next
    current_node.next = None
    del del_node
    return head

# Traversal of the DLL
def display(head):
  
    current_node = head
    while current_node:
        print(current_node.data, end = " <-> ")
        current_node = current_node.next
    print("None")

# Create nodes
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Link nodes
head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

# Delete the first node
head = delete_at_beginning(head)

display(head)

# Delete at given position
head = delete_at_given_position(head, 2)
display(head)

# Delete last node
head = delete_at_end(head)
display(head)