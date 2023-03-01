#Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

Tree = BinaryTree()
Tree.root = Node(1)
Tree.root.left = Node(2)
Tree.root.right = Node(3)
print(Tree.root.data)