class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        itr = self
        while itr.parent:
            level += 1
            itr = itr.parent
            
        return level

    def print_tree(self):
        
        spaces = '--' * self.get_level()
        print(spaces  + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()




def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    phone = TreeNode("Phone")

    pc = TreeNode("pc")

    laptop.add_child(pc)
    laptop.add_child(TreeNode("desktop"))

    
    root.add_child(laptop)
    root.add_child(phone)


    return root

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()


    