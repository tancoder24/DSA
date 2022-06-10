class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Cll:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        
        node = Node(data)

        temp = self.head
        node.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next

            temp.next = node
        else:
            node.next = node

        self.head = node

    def print_values(self):
        temp = self.head

        while (True):
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break

        # while temp.next != self.head:
        #     print(temp.data)
        #     temp = temp.next
        # else:
        #     print(temp.data)

if __name__ == "__main__":
    
    Cll_obj = Cll()

    Cll_obj.insert_at_beginning(1)  
    Cll_obj.insert_at_beginning(2)  
    Cll_obj.insert_at_beginning(3)  
    Cll_obj.insert_at_beginning(4)        
    Cll_obj.insert_at_beginning(5)        
    Cll_obj.insert_at_beginning(6)   

    Cll_obj.print_values()     


