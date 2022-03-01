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
        length = self.length()
        if index < 0 or index >= length:
            print("index out of range")
            return

        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        elif index == length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        count = 0
        itr = self.head
        while(itr):
            if count == index:
                itr.next.prev, itr.prev.next = itr.prev, itr.next
                return
            itr = itr.next
            count += 1        

    def insert_at_index(self, index, value):
        if index == 0:
            self.insert_at_beginning(value)
            return

        elif index == self.length():
            self.insert_at_end(value)
            return

        count = 0
        itr = self.head
        while(itr):
            if count == index - 1:
                itr.next = Node(value, itr, itr.next)
                return
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        self.tail = None

        for data in data_list:
            self.insert_at_end(data)

    def remove_value(self, data):
        itr = self.head

        while (itr):
            if itr.data == data:
                if itr.prev is None:
                    self.head = itr.next
                    self.head.prev = None
                    return

                elif itr.next is None:
                    self.tail = itr.prev
                    self.tail.next = None
                    return

                itr.prev.next, itr.next.prev = itr.next, itr.prev
                return
            itr = itr.next

        print("value not found")

    def insert_after_value(self, data_after, data_to_insert):
        # itr = self.head

        # while(itr):
        #     if itr.data == data_after:
        #         node = Node(data_to_insert, )
        #         return
        #     itr = itr.next

        # print(f"{data_after} not found")
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
        if self.head is None and self.tail is None:
            return 0

        count = 0
        itr = self.head
        while(itr):
            count += 1
            itr = itr.next

        return count

if __name__ == "__main__":

    dll = DoubleLinkedList()

    dll.insert_at_beginning(1)
    dll.insert_at_beginning(2)
    dll.insert_at_beginning(3)
    dll.insert_at_beginning(4)
    dll.insert_at_end(5)

    dll.print_forward()

    dll.insert_values([10,20,30,40,50])
    dll.remove_value(60)
    dll.print_forward()