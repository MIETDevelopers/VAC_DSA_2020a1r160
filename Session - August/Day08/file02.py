class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def maxDepth(node):
    if node is None:
        return 0
    else:
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        if (lDepth > rDepth):
            return lDepth + 1
        else :
            return rDepth + 1
        # ek line rehti hai        

def isBalanced(root):
    lht  = maxDepth(root.left)
    rht = maxDepth(root.right)
    return abs(lht -rht) <2

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.left.left = Node(60)
        
print(isBalanced(root))

print("Height of the tree is %d" % (maxDepth(root)))
h = maxDepth(root)