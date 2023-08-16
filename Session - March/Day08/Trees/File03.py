#Pathlogical Tree
#A tree where every initial node has one child such trees are same as linked list.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if node:
        print(node.value, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.left = Node(4)
root.left.left.left.left = Node(5)

pre_order_traversal(root)