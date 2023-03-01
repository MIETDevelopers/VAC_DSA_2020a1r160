# find level
class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
def finddistance(root, n1, n2):
    global ans
    if not root:
        return 0
    left = finddistance(root.left, n1,n2)
    right = finddistance(root.right, n1, n2)
    if root.data == n1 or root.data == n2:
        if left or right:
            ans = max(left, right)
            return 0
        else:
            return 1
    elif left and right:
        ans = left+right
        return 0
    elif left or right:
        return max(left,right)+1
    return 0
        
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
def finddist(root, n1,n2):
    ans = finddistance(root, n1, n2)
    return ans
Tree = BinaryTree()
Tree.root = Node(1)
Tree.root.left = Node(2)
Tree.root.right = Node(3)
Tree.root.left.left = Node(5)
Tree.root.right.left = Node(6)
Tree.root.right.right = Node(7)
print("Level:")
print(printLevel(Tree.root, 7))
print("Distance:")
print(finddist(Tree.root, 4, 5))