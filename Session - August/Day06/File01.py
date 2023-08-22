#A Program to print left view of a complete binary tree based on dynamic user input but first ask for height of tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(height):
    if height <= 0:
        return None
    
    root = TreeNode(int(input("Enter value for root: ")))
    queue = [root]
    level = 1
    while level < height:
        node = queue.pop(0)
        
        left_val = int(input(f"Enter left child value for {node.val}: "))
        if left_val != -1:
            node.left = TreeNode(left_val)
            queue.append(node.left)
        
        right_val = int(input(f"Enter right child value for {node.val}: "))
        if right_val != -1:
            node.right = TreeNode(right_val)
            queue.append(node.right)
        
        level += 1
    
    return root

def leftView(root):
    if not root:
        return
    
    queue = [root]
    while queue:
        count = len(queue)
        for i in range(count):
            node = queue.pop(0)
            if i == 0:
                print(node.val, end=" ")
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def main():
    height = int(input("Enter the height of the binary tree: "))
    root = buildTree(height)
    
    print("Left view of the binary tree:")
    leftView(root)

if __name__ == "__main__":
    main()