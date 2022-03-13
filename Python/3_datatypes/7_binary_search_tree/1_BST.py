class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_node(self, val):
        if self.data == val:
            return
        elif val < self.data:
            if not self.left:
                self.left = BinarySearchTreeNode(val)
                return
            self.left.add_node(val)
        
        elif self.data < val:
            if not self.right:
                self.right = BinarySearchTreeNode(val)
                return
            self.right.add_node(val)

    def search_tree(self, val):
        if self.data == val:
            return True
        
        elif val < self.data and self.left:
            return self.left.search_tree(val)

        elif self.data < val and self.right:
            return self.right.search_tree(val)
        
        else:
            return False

    def find_min(self):
        itr = self
        while(itr.left):
            itr = itr.left
        return itr.data

    def find_max(self):
        itr = self
        while(itr.right):
            itr = itr.right
        return itr.data
    
    def calculate_sum(self):
        elements = self.inorder_traversal()
        return sum(elements)

    def inorder_traversal(self):
        elements = []
        if self.left:
            elements.extend(self.left.inorder_traversal())  
        elements.append(self.data)
        if self.right:
            elements.extend(self.right.inorder_traversal())
        return elements

    def preorder_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements.extend(self.left.preorder_traversal())
        if self.right:
            elements.extend(self.right.preorder_traversal())
        return elements

    def postorder_traversal(self):
        elements = []
        if self.left:
            elements.extend(self.left.postorder_traversal())
        if self.right:
            elements.extend(self.right.postorder_traversal())
        elements.append(self.data)
        return elements

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for element in elements[1:]:
        root.add_node(element)

    return root

if __name__ == "__main__":

    # tree creation
    bst = build_tree([15,12,7,14,27,20,88,23])

    # tree traversal
    print( bst.inorder_traversal() )
    print( bst.preorder_traversal() )
    print( bst.postorder_traversal() )

    # search tree
    print(bst.search_tree(150))

    # Find min / max / sum
    print( bst.find_min() )
    print( bst.find_max() )
    print( bst.calculate_sum() )
