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
    
    ll.insert_at_beginning(10)
    ll.insert_values([1,2,3,4,5])
    ll.insert_at_index(5, 14)
    ll.print()
    print( ll.length() )
