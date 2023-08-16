#Full Binary Tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def isFullTree(root):
    if not root:
        return True
  
    if not root.left and not root.right:
        return True  

    if root.left and root.right:
        return (isFullTree(root.left) and isFullTree(root.right))
    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

if isFullTree(root):
    print("The tree is a Full Binary Tree")
else:
    print("The tree is not a Full Binary Tree")