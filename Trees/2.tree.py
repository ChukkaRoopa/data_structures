# Tree to print only name , designation or both

class TreeNode:
    def __init__(self, data, designation):
        self.data = data
        self.designation = designation
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

    def print_tree(self, mode = "both"):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        designation_info = f" ({self.designation})" if self.designation is not None else ' '

        if mode == "both":
            print(prefix + self.data + designation_info)

        elif mode == "name":
            print(prefix + self.data)

        elif mode == "designation":
            print(prefix + designation_info)

        if self.children:
            for child in self.children:
                child.print_tree(mode)
    
def build_node():
    root = TreeNode("Nilupul", "CEO")

    parent1 = TreeNode("Chinmay", "CTO")

    Vishwa = TreeNode("Vishwa", "Infastructure Head")

    Vishwa.add_child(TreeNode('Dhaval', 'Cloud Manager'))
    Vishwa.add_child(TreeNode('Abhijit', 'App Manager'))

    parent1.add_child(Vishwa)
    parent1.add_child(TreeNode("Aamir", 'Application Head'))

    parent2 = TreeNode("Gels", 'HR Head')
    parent2.add_child(TreeNode("Peter", 'Recruitment Manager'))
    parent2.add_child(TreeNode("Waqas",'Policy Manager'))

    root.add_child(parent1)
    root.add_child(parent2)

    root.print_tree("both")
    root.print_tree("name")
    root.print_tree("designation")

if __name__=='__main__':
    build_node()