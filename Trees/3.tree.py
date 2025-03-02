# Print Tree based on levels

class TreeNode:
    def __init__(self, data, price=None):
        self.data = data
        self.price = price
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p=p.parent
        return level

    def print_tree(self, level=-1):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        price_info = f"( Rs. {self.price})" if self.price is not None else ' '

        if level==-1 or self.get_level() <= level:
            print(prefix + self.data + price_info)

        if self.children:
            for child in self.children:
                child.print_tree(level)
    
def build_node():
    root = TreeNode("Electronics")

    parent1 = TreeNode("Laptop")
    macbook = TreeNode("Macbook", 100000)
    macbook.add_child(TreeNode('m1', 900000))
    macbook.add_child(TreeNode('m2'))
    macbook.add_child(TreeNode('m3'))

    parent1.add_child(macbook)
    parent1.add_child(TreeNode("Dell"))
    parent1.add_child(TreeNode("Lenovo"))

    parent2 = TreeNode("Television")
    parent2.add_child(TreeNode("Sony"))
    parent2.add_child(TreeNode("LG"))
    parent2.add_child(TreeNode("Samsung"))

    parent3 = TreeNode("Phone")
    parent3.add_child(TreeNode("Vivo"))
    parent3.add_child(TreeNode("Apple"))
    parent3.add_child(TreeNode("Redmi"))

    root.add_child(parent1)
    root.add_child(parent2)
    root.add_child(parent3)

    root.print_tree()
    root.print_tree(0)
    root.print_tree(1)
    root.print_tree(2)

if __name__=='__main__':
    build_node()