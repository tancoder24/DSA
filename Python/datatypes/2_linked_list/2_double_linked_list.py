class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.next = next
        self.prev = prev
    
class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def get_last_node(self):
        itr = self.head
        while (itr.next):
            itr = itr.next
        return itr

    def length(self):
        if self.head is None:
            return 0
        count = 0
        itr = self.head
        while(itr):
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        node = Node(data, None, self.head)
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return

        itr = self.get_last_node()
        node = Node(data, itr, None)
        itr.next = node

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at_index(self, index, value):
        if index < 0 or index > self.length():
            print("index out of range")
            return

        elif index == 0:
            self.insert_at_beginning(value)
            return

        elif index == self.length():
            self.insert_at_end(value)
            return

        count = 0
        itr = self.head
        while(itr):
            if count == index - 1:
                node = Node(value, itr, itr.next)
                itr.next.prev = node
                itr.next = node
                return
            itr = itr.next
            count += 1

    def remove_at_index(self, index):
        length = self.length()
        if index < 0 or index >= length:
            print(f"index {index} out of range")
            return

        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while(itr):
            if count == index:
                if itr.next is None:
                    itr.prev.next = None
                    return

                itr.prev.next, itr.next.prev = itr.next, itr.prev
                return
            itr = itr.next
            count += 1        

    def remove_value(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head
        while(itr):
            if itr.data == data:
                if itr.next == None:
                    itr.prev.next = None
                    return
                itr.prev.next, itr.next.prev = itr.next, itr.prev
            itr = itr.next
        print(f"{data} value not found")

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head

        while(itr):
            if itr.data == data_after:
                if itr.next == None:
                    self.insert_at_end(data_to_insert)
                    return
                node = Node(data_to_insert, itr, itr.next)
                itr.next.prev = node
                itr.next = node
                return
            itr = itr.next

        print(f"{data_after} not found and {data_to_insert} not inserted")

    def print_forward(self):
        if self.head is None:
            print("Linked List Empty")
            return

        itr = self.head
        dllstr = ""  
        while(itr):
            dllstr += str(itr.data) + " --> "
            itr = itr.next
        print(dllstr)

    def print_backword(self):
        if self.head is None:
            print("Linked List Empty")
            return

        itr = self.get_last_node()
        dllstr = "" 
        while(itr):
            dllstr += str(itr.data) + " --> "
            itr = itr.prev
        print(dllstr)



if __name__ == "__main__":

    dll = DoubleLinkedList()

    dll.insert_values([10,20,30,40,50])
    dll.insert_after_value(60,100)

    dll.print_forward()
    dll.print_backword()