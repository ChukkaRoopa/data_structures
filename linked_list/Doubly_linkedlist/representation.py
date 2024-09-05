'''
Doubly linked list : Doubly Linked List (DLL) is a special type of linked list in which each node contains a pointer to the previous
node as well as the next node of the linked list. In a Doubly Linked List, we can traverse in forward and backward direction using
the next and previous pointer respectively.
'''

# Representation of Doubly linked list 
class Node:
    def __init__(self):
        # reference to next node
        self.next = None
        # reference to prev node
        self.prev = None
        self.data = None
