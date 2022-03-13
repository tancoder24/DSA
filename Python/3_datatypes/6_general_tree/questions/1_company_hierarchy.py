class TreeNode:
    def __init__(self, name, designation):
        self.data = [name, designation]
        self.parent = None
        self.children = []

    def add_child(self, node):
        node.parent = self
        self.children.append(node)

    def print_tree(self, type):
        level = self.get_level()
        if level:
            print( "   "*level + "|__", end="" )
        
        if type == "both":
            print(self.data[0] + f" ({self.data[1]})")
        elif type == "name":
            print(self.data[0])
        elif type == "designation":
            print(f"({self.data[1]})")

        for child in self.children:
            child.print_tree(type)

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

def build_management_tree():
    # level 0
    ceo = TreeNode("Nilupul", "CEO")
    
    # level 1
    cto = TreeNode("Chinmay", "CTO")
    hr_head = TreeNode("Gels", "HR Head")

    ceo.add_child(cto)
    ceo.add_child(hr_head)

    # level 2
    infra_head = TreeNode("Vishwa", "Infrastructure Head")
    application_head = TreeNode("Aamir", "Application Head")
    recruitment_manager = TreeNode("Peter", "Recruitment Manager")
    policy_manager = TreeNode("Waqas", "Policy Manager")

    cto.add_child(infra_head)
    cto.add_child(application_head)
    hr_head.add_child(recruitment_manager)
    hr_head.add_child(policy_manager)

    # level 3
    cloud_manager = TreeNode("Dhaval", "Cloud Manager")
    app_manager = TreeNode("Abhijit" , "App Manager")

    infra_head.add_child(cloud_manager)
    infra_head.add_child(app_manager)

    return ceo

if __name__ == "__main__":
    root = build_management_tree()
    root.print_tree("both")