#Level order, preorder, postorder....
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def levelOrderTraversal(root):
    if not root:
        return
    queue = [root]
    while queue:
        curr = queue.pop(0)
        print(curr.value, end=' ')
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

def preOrderTraversal(root):
    if not root:
        return
    print(root.value, end=' ')
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def postOrderTraversal(root):
    if not root:
        return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.value, end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level-order Traversal: ")
levelOrderTraversal(root)
print("\nPre-order Traversal: ")
preOrderTraversal(root)
print("\nPost-order Traversal: ")
postOrderTraversal(root)