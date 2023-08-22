#Create a program to print left side of a binary tree based on dynamic user input
def print_left_side_of_tree(tree):
    if tree == None:
        return
    print(tree.data)
    print_left_side_of_tree(tree.left)
    print_left_side_of_tree(tree.right)
def input_dynamic_tree():
    data = input("Enter data: ")
    if data == "x":
        return None
    tree = Tree(data)
    tree.left = input_dynamic_tree()
    tree.right = input_dynamic_tree()
    return tree
def main():
    tree = input_dynamic_tree()
    print_left_side_of_tree(tree)