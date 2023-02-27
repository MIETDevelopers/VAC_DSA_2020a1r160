class Node:
    def __init__(self,k):
        self.key = k
        self.next = None
def rev(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr 
        curr = next 
    return prev
def printL(head):
    while head:
        print(head.key , end=" -> ")
        head = head.next 
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)+
a=rev(head)
printL(a)