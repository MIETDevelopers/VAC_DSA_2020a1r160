class newNode:

    # Constructor to create a newNode
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right  = None
        
    

# A utility function to insert a new
# Node with given key in BST


def insert(root, key):

    # Create a new Node containing
    # the new element
    newnode = newNode(key)

    # Pointer to start traversing from root
    # and traverses downward path to search
    # where the new node to be inserted
    x = root #(50 and 30's address)

    # Pointer y maintains the trailing
    # pointer of x
    y = None

    while (x != None):
        y = x # (50's address is 1000)
        if (key < x.key):
            x = x.left
        else:
            x = x.right

    # If the root is None i.e the tree is
    # empty. The new node is the root node
    if (y == None):
        y = newnode #(50 inserted)

    # If the new key is less than the leaf node key
    # Assign the new node to be its left child
    elif (key < y.key):
        y.left = newnode

    # else assign the new node its
    # right child
    else:
        y.right = newnode

    # Returns the pointer where the
    # new node is inserted
    return y

# A utility function to do inorder
# traversal of BST


def Inorder(root):

    if (root == None):
        return
    else:
        Inorder(root.left)
        print(root.key, end=" ")
        Inorder(root.right)



root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 45)
insert(root, 60)
insert(root, 10)
root.findval(30)
root.findval(20)

    # Pr inorder traversal of the BST



