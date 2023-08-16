#Skewed Binary tree.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def printTree(root):
    if root is None:
        return
    print(root.data, end=' ')
    printTree(root.right)

root = None
keys = [10, 5, 15, 20, 25]
for key in keys:
    root = insert(root, key)
print("Skewed Binary Tree:")
printTree(root)