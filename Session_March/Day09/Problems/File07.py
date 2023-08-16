#Appending lists to a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        
    def append_list(self, lst):
        for item in lst:
            self.insert(item)

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end='->')
            temp = temp.next
linked_list = LinkedList()
lst = [1,2,9,0,4,11,13]
linked_list.append_list(lst)
linked_list.printList()