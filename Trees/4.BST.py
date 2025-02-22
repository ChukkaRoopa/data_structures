# Every node has at most 2 nodes
# Elements to the left of the current node are always less than the current node and similar case with right nodes
# should not contain duplicate nodes
# Search complexity - O(log N)
# Insert Complexity - O(log N)

# Traversal Techniques of BST - 
        # 1. Breadthfirst Search
        # 2. Depthfirst search - inorder, preorder , postorder traversal
        
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:        
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def inorder_traversal(self):

        elements = []
        
        # Visit left tree
        if self.left:
            elements += self.left.inorder_traversal()

        # visit root node
        elements.append(self.data)

        # Visit right tree
        if self.right:
            elements += self.right.inorder_traversal()

        return elements
    
    def preorder_traversal(self):

        elements = []

        # visit root node
        elements.append(self.data)
        
        # Visit left tree
        if self.left:
            elements += self.left.preorder_traversal()

        # Visit right tree
        if self.right:
            elements += self.right.preorder_traversal()

        return elements
    
    def postorder_traversal(self):

        elements = []

        # Visit left tree
        if self.left:
            elements += self.left.postorder_traversal()

        # Visit right tree
        if self.right:
            elements += self.right.postorder_traversal()

        # visit root node
        elements.append(self.data)        

        return elements
    
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            # value will be in left sub tree
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            # Value will be in right sub tree
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def delete(self, val):
        # if value is less than node
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        # if value is greater than node
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)    
        # if value is equal to node -> val ==  self.data
        else:
            # if node has no child
            if self.left is None and self.right is None:
                return None
            # if node has one child
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            # if node have two children
            # delete node by taking min_value of right subtree
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)

            # (or)
            # delete node by taking max_value of left subtree
            # max_value = self.left.find_max()
            # self.data = max_value
            # self.left = self.left.delete(max_value)
        return self

def build_node(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__=="__main__":
    numbers = [15,27,20,88,23,12,7,14]
    numbers_tree = build_node(numbers)

    print('inorder traversal: ', numbers_tree.inorder_traversal())
    print('preorder traversal: ', numbers_tree.preorder_traversal()) 
    print('postorder traversal: ', numbers_tree.postorder_traversal()) 
    print(numbers_tree.search(99))  
    print(numbers_tree.search(3))  
    print('min_value: ', numbers_tree.find_min())  
    print('max_value: ', numbers_tree.find_max())  
    numbers_tree.delete(14)
    numbers_tree.delete(88)
    print('inorder traversal: ', numbers_tree.inorder_traversal()) 