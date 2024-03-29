class BinaryTree:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
 
    def set_root(self, key):
        self.key = key
 
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.key, end=' ')
        if self.right is not None:
            self.right.inorder()
 
    def insert_left(self, new_node):
        self.left = new_node
 
    def insert_right(self, new_node):
        self.right = new_node
 
    def search(self, key):
        if self.key == key:
            return self
        if self.left is not None:
            temp =  self.left.search(key)
            if temp is not None:
                return temp
        if self.right is not None:
            temp =  self.right.search(key)
            return temp
        return None
 
 
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def sum_nodes(node):
    if node is None:
        return 0
    return node.key + sum_nodes(node.left) + sum_nodes(node.right)
 
 
btree = None
 
print('Menu (this assumes no duplicate keys)')
print('insert <data> at root')
print('insert <data> left of <data>')
print('insert <data> right of <data>')
print('count')
print('sum')
print('quit')
 
while True:
    print('inorder traversal of binary tree: ', end='')
    if btree is not None:
        btree.inorder()
    print()
 
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        new_node = BinaryTree(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
                btree = new_node
        else:
            position = do[4].strip().lower()
            key = int(position)
            ref_node = None
            if btree is not None:
                ref_node = btree.search(key)
            if ref_node is None:
                print('No such key.')
                continue
            if suboperation == 'left':
                ref_node.insert_left(new_node)
            elif suboperation == 'right':
                ref_node.insert_right(new_node)
 
    elif operation == 'count':
        print('Number of nodes in tree: {}'.format(count_nodes(btree)))
        
    elif operation == 'sum':
        print('Sum of nodes in tree: {}'.format(sum_nodes(btree)))
 
    elif operation == 'quit':
        break
