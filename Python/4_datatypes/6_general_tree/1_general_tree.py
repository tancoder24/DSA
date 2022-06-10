class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        level = self.get_level()
        if level > 0:
            print(("   "*level)+"|__", end="")
        print(self.data)
        for child in self.children:
            child.print_tree()

    def get_level(self):
        level = 0
        parent = self.parent
        while(parent):
            level += 1
            parent = parent.parent
        return level

def build_product_tree():
    # Level 0
    root = TreeNode("Electronics")

    # Level 1
    laptop = TreeNode("Laptop")
    phone = TreeNode("Phone")
    
    # Level 2
    # laptop
    hp = TreeNode("HP")
    dell = TreeNode("Dell")
    acer = TreeNode("Acer")
    # phone
    mi = TreeNode("MI")
    samsung = TreeNode("SAMSUNG")
    iphone = TreeNode("IPHONE")

    # adding child
    root.add_child(laptop)
    root.add_child(phone)

    laptop.add_child(hp)
    laptop.add_child(dell)
    laptop.add_child(acer)

    phone.add_child(mi)
    phone.add_child(samsung)
    phone.add_child(iphone)

    return root

if __name__ == "__main__":
    root = build_product_tree()

    root.print_tree()

    # hp level
    hp = root.children[0].children[0]
    level =  root.children[0].children[0].get_level()
    print(hp.data, "-->", level)
