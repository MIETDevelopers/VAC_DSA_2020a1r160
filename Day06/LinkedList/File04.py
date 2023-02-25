class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    # def push(self, data):
    #     New = Node(data)
    #     temp = self.head.next
    #     self.head.next = New
    #     New.next =  temp
    #     New.prev =self.head
    def insert(self, head, data):
        temp = head
        curr = Node(data)
        curr.next = head
        temp.prev = curr
        self.head = curr
        
        
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end = "->")
            temp = temp.next

llist = Linkedlist()
llist.head = Node(1)
llist.insert(llist.head, 2)
llist.insert(llist.head, 3)
llist.printlist()