# Binary Tree in Python

class Node:
    def __init__(balaji, key):
        balaji.left = None
        balaji.right = None
        balaji.val = key

    # Traverse preorder
    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')


root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node(4)
root.right.right = Node(50)
root.right.right.left = Node(60)
root.right.left = Node(70)
root.right.left.right = Node(80)
root.right.left.right.right = Node(90)
root.right.right.left.right = Node(100)


print("Pre order Traversal: ", end="")
root.traversePreOrder()
print("\nIn order Traversal: ", end="")
root.traverseInOrder()
print("\nPost order Traversal: ", end="")
root.traversePostOrder()
