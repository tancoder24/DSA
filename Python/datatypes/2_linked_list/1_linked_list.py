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

    def remove_at_index(self, index):
        if index < 0 or index >= self.length():
            print("invalid index")
            return
        
        elif index == 0:
            self.head = self.head.next  
            return

        count = 0
        itr = self.head
        while( itr.next ):
            if count == index-1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def insert_at_index(self, index, value):
        if index < 0 or index > self.length():
            print("index out of range")
            return

        elif index == 0:
            self.insert_at_beginning(value)

        itr = self.head
        count = 0
        while(itr.next):
            if count == index-1:
                itr.next = Node(value, itr.next)
                break
            count += 1
            itr = itr.next

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_value(self, data):
        if self.head == None:
            print("Linked List empty")
            return

        elif self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while( itr.next ):
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next

        print("Value not found")
        return

    def insert_after_value(self, data_after, data_to_insert):
        
        if self.head is None:
            return

        itr = self.head

        while(itr):
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                return
            itr = itr.next

        print("data after not found")

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

    def length(self):
        itr = self.head
        count =  0

        while(itr):
            itr = itr.next
            count += 1

        return count

if __name__ == "__main__":
    ll = LinkedList()
    
    
    ll.insert_values([1,2,3,4,5])
    ll.insert_after_value(5,12)

    ll.print()
    print( ll.length() )
