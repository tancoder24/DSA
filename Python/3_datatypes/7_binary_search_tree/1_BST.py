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

    def delete(self, val):
        if val < self.data and self.left:
            self.left = self.left.delete(val)
        elif self.data < val and self.right:
            self.right = self.right.delete(val)

        elif val == self.data:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            max_value = self.left.find_max()
            self.data = max_value
            self.left = self.left.delete(max_value)

            # 1st Way
            # min_value = self.right.find_min()
            # self.data = min_value
            # self.right = self.right.delete(min_value)

        return self 

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
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
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

    # delete value
    bst.delete(88)
    print( bst.inorder_traversal() )