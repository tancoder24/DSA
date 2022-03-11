class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, val):
        if self.head == None:
            self.head = Node(val)
            return
        
        itr = self.head
        while ( itr.next):
            itr = itr.next

        itr.next = Node(val)
    
    def add_list(self, arr):
        for a in arr:
            self.insert_at_end(a)

    def print_list(self):
        itr = self.head
        while(itr.next):
            print(itr.val)
            itr = itr.next

    def reverseList(self, itr=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            head = self.head
        
        arr = []
        arr.append(head.val)
        


        while (head.next):
            arr.extend(self.reverseList( head.next ))
        return arr


ll = LinkedList()
ll.add_list([1,2,3,4])

ll.reverseList()
# ll.print_list()

