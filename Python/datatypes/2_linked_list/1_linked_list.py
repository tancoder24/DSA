class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List empty")
            return

        itr = self.head
        llstr = ""

        while(itr):
            llstr += str(itr.data) + " --> "
            itr = itr.next
        
        print(llstr + "Null")


if __name__ == "__main__":
    ll = LinkedList()
    
    ll.add_at_beginning(10)
    ll.add_at_beginning(20)

    ll.print()
