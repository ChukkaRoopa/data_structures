# Insertion of the DLL

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

# insert at begin
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

# insert after a given node
def insert_after_node(node, data):
    new_node = Node(data)
    if node is None:
        print("Node not found")
        return
    
    new_node.next =  node.next
    new_node.prev =  node
    if node.next:
        node.prev = new_node
    node.next = new_node

# Insert before a given node
def insert_before_node(node, data):
    if node is None:
        print("Node not found")
        return
    
    new_node = Node(data)
    new_node.next = node
    new_node.prev = node.prev

    if node.prev:
        node.prev.next = new_node
    node.prev = new_node

# Insert at the end 
def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return  new_node
    
    current_node = head
    while current_node.next:
        current_node = current_node.next
    current_node.next = new_node
    new_node.prev = current_node
    return head

# Traversal of the node
def display(head):
    current_node = head
    while current_node:
        print(current_node.data, end = " <-> ")
        current_node = current_node.next
    print("None")

head = None
head = insert_at_beginning(head, 4)
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 1)
print("Insertion at beginning")
display(head)

insert_at_end(head, 8)
print("Insert at end")
display(head)

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

print("DLL before insertion:")
display(head)

insert_after_node(node2, 5)

print("Insertion after a given node")
display(head)

insert_before_node(node4, 6)
print("Insertion before a given node")
display(head)