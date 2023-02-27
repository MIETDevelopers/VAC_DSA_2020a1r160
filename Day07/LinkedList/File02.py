 # Circular linked list using python.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        self.head = new_node
        current.next = self.head

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def print_list(self):
        if self.head is None:
            return
        current = self.head
        while current.next != self.head:
            print(current.data, end=' ')
            current = current.next
        print(current.data, end=' ')

if __name__ == '__main__':
    cll = CircularLinkedList()
    cll.add_at_beginning(1)
    cll.add_at_end(2)
    cll.add_at_end(3)
    cll.add_at_end(4)
    cll.add_at_end(5)
    cll.add_at_beginning(6)
    cll.print_list()