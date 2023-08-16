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

    def delete_node(self, data):
        if self.head is None:
            return
        current = self.head
        previous = None
        while current.next != self.head:
            if current.data == data:
                break
            previous = current
            current = current.next
        if current == self.head and current.data == data:
            if current.next != self.head:
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            else:
                self.head = None
        elif current.data == data:
            previous.next = current.next
        else:
            print("Node not found in the circular linked list")

    def swap_nodes(self, x, y):
        if x == y:
            return
        prevX = None
        currentX = self.head
        while currentX and currentX.data != x:
            prevX = currentX
            currentX = currentX.next
        prevY = None
        currentY = self.head
        while currentY and currentY.data != y:
            prevY = currentY
            currentY = currentY.next
        if not currentX or not currentY:
            return
        if prevX:
            prevX.next = currentY
        else:
            self.head = currentY
        if prevY:
            prevY.next = currentX
        else:
            self.head = currentX
        currentX.next, currentY.next = currentY.next, currentX.next

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
    cll.print_list()
    print()
    cll.delete_node(3)
    cll.print_list()