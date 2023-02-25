#Linked list python program.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end='->')
            temp = temp.next
lst = LinkedList()
n1 = Node(5)
n2 = Node(6)
n3 = Node(7)
lst.head = n2
n2.next=n1
n1.next=n3
lst.printList()