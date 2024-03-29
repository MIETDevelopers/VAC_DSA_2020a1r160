"""
full binary tree


infix to prefix
reverse: f+(e*d) -c/b+a

f            f
+      +     f
(      +(    f
e            fe
*       +(*  fe
d             fed
)       +      fed*
-       -      fed*+
c               c
/       -/     fed*+c
b              fed*+cb
+       +       fed*+cb/-
a               fed*+cb/-a
fed*+cb/-a+

reverse: +a-/bc+*def
"""

# A program to represent a full binary tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            temp=self.root
            while True:
                if data<temp.data:
                    if temp.left==None:
                        temp.left=Node(data) # type: ignore
                        break
                    else:
                        temp=temp.left
                elif data>temp.data:
                    if temp.right==None:
                        temp.right=Node(data) # type: ignore
                        break
                    else:
                        temp=temp.right
                else:
                    break
    def preorder(self,temp):
        if temp!=None:
            print(temp.data,end=" ")
            self.preorder(temp.left)
            self.preorder(temp.right)
    def inorder(self,temp):
        if temp!=None:
            self.inorder(temp.left)
            print(temp.data,end=" ")
            self.inorder(temp.right)
    def postorder(self,temp):
        if temp!=None:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.data,end=" ")
    def display(self):
        print("Preorder Traversal:")
        self.preorder(self.root)
        print("\nInorder Traversal:")
        self.inorder(self.root)
        print("\nPostorder Traversal:")
        self.postorder(self.root)
t=Tree()
t.insert(50)
t.insert(30)
t.insert(70)
t.insert(20)
t.insert(40)
t.insert(60)
t.insert(80)
t.display()
