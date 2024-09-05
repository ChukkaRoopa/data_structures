class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

def traversal(head):
    current_node = head
    while(current_node):
        print(current_node.data, end = " <-> ")
        current_node = current_node.next
    print("None")

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

head = None
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 1)

traversal(head)