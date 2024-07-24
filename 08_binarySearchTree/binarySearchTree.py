class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def add_child(self,data):
        #if already exists
        if data == self.data:
            return

        if data < self.data:
            #we add the data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()


        #visit base node:
        elements.append(self.data)



        #right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def search(self, val):
        if val == self.data:
            return True
        
        if val < self.data:
            if self.left:
               return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
               return self.right.search(val)
            else:
                return False
    
    def find_min(self):
        # elements = self.in_order_traversal()
        # return elements[0]
        itr = self
        element = self.data
        while itr.left:
            element = itr.left.data
            itr = itr.left

        return element
    
    def find_max(self):
        # elements = self.in_order_traversal()
        # return elements[-1] #stack peek
        itr = self
        element = self.data
        while itr.right:
            element = itr.right.data
            itr = itr.right

        return element
    
    def calculate_sum(self):
        return sum(self.in_order_traversal())
    
def post_order_traversal(node: BinarySearchTreeNode):
    if node is None:
        return
    
    post_order_traversal(node.left)
    post_order_traversal(node.right)


    print(node.data, end= ' ')
        
def pre_order_traversal(node: BinarySearchTreeNode):
    if node is None:
        return
    
    print(node.data, end= ' ')
    
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

                


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root
    

if __name__ == '__main__':
    numbers = [17, 4 , 2 ,36, 5 , 6 ,8]
    root = build_tree(numbers)
    print(root.in_order_traversal())
    #print(root.find_max())
    #print(root.find_min())
    #print(root.calculate_sum())
    post_order_traversal(root)
    pre_order_traversal(root)
   