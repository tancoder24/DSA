class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.next = next
        self.prev = prev
    
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        if self.head is None and self.tail is None:
            node = Node(data)
            self.head = node
            self.tail = node
            return

        node = Node(data, None, self.head)
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None and self.tail is None:
            node = Node(data)
            self.head = node
            self.tail = node
            return

        node = Node(data, self.tail, None)
        self.tail.next = node
        self.tail = node

    def remove_at_index(self, index):
        pass

    def insert_at_index(self, index, value):
        pass

    def insert_values(self, data_list):
        pass

    def remove_value(self, data):
        pass

    def insert_after_value(self, data_after, data_to_insert):
        pass

    def print_forward(self):
        itr = self.head
        dllstr = "Head --> "  

        while(itr):
            dllstr += str(itr.data) + " --> "
            itr = itr.next
        dllstr += "Tail"

        print(dllstr)

    def print_backword(self):
        itr = self.tail
        dllstr = "Tail <-- " 

        while(itr):
            dllstr += str(itr.data) + " <-- "
            itr = itr.prev
        dllstr += "Head"

        print(dllstr)

    def length(self):
        pass

if __name__ == "__main__":

    dll = DoubleLinkedList()

    dll.insert_at_beginning(1)
    dll.insert_at_beginning(2)
    dll.insert_at_beginning(3)
    dll.insert_at_beginning(4)
    dll.insert_at_end(5)

    dll.print_forward()
    dll.print_backword()