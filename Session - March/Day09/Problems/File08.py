#Binary tree to Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def convert_to_linked_list(root, head=None):
    if not root:
        return head

    head = convert_to_linked_list(root.right, head)
    root.right = head
    if head:
        head.left = root
    head = root
    head = convert_to_linked_list(root.left, head)
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.right

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
head = convert_to_linked_list(root)

print_linked_list(head)