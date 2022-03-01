class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return

        itr = self.head
        while(itr.next):
            itr = itr.next
        
        itr.next = Node(data, None)

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
    
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)

    ll.print()
