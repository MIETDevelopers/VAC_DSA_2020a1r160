#Singly linked list
class Node:
    def __init__(self, data):
        self.data  =  data
        self.next  =  None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def addNode(self, data):
        New = Node(data)
        temp  = self.head
    def deleteNode(node):
        curr = node
        while curr.next:
            curr = curr.next
            prev =  curr
        print(prev)
        while(temp.next):
            temp =  temp.next
        #temp.next =  New
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data, end = "->")
            temp =  temp.next
        print("NULL")

lst = LinkedList()
N1 = Node(5)
lst.head = N1
lst.addNode(6)
lst.addNode(7)
lst.printlist()