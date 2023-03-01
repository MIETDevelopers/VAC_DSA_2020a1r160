# find level
class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
def printLevel(root, x):
    if root is None:
        return 0
    q = []
    current_level = 1
    q.append(root)
    while(len(q)>0):
        size  =  len(q)
        for i in range(size):
            node = q.pop(0)
            if node.data == x:
                return current_level
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        current_level += 1
    return 0
Tree = BinaryTree()
Tree.root = Node(1)
Tree.root.left = Node(2)
Tree.root.right = Node(3)
Tree.root.left.left = Node(5)
Tree.root.right.left = Node(6)
Tree.root.right.right = Node(7)
print(printLevel(Tree.root, 7))