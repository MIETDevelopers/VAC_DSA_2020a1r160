#Operations for linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, previous_node, data):
        if not previous_node:
            print("previousious node is not in the list")
            return
        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def delete_node(self, key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        previous_node = None
        while curr_node and curr_node.data != key:
            previous_node = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        previous_node.next = curr_node.next
        curr_node = None

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return
        previous_node_1 = None
        curr_node_1 = self.head
        while curr_node_1 and curr_node_1.data != key_1:
            previous_node_1 = curr_node_1
            curr_node_1 = curr_node_1.next
        previous_node_2 = None
        curr_node_2 = self.head
        while curr_node_2 and curr_node_2.data != key_2:
            previous_node_2 = curr_node_2
            curr_node_2 = curr_node_2.next
        if not curr_node_1 or not curr_node_2:
            return
        if previous_node_1:
            previous_node_1.next = curr_node_2
        else:
            self.head = curr_node_2
        if previous_node_2:
            previous_node_2.next = curr_node_1
        else:
            self.head = curr_node_1
        curr_node_1.next, curr_node_2.next = curr_node_2.next, curr_node_1.next

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next

# Example usage
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.print_list()
print('\n')
llist.prepend("E")
llist.insert_after_node(llist.head.next, "F")
llist.delete_node("B")
llist.swap_nodes("E", "C")
llist.print_list()