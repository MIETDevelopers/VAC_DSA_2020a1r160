#Distance between two nodes
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
def find_level(root, value, level):
    if root is None:
        return 0
    if root.value == value:
        return level
    left_level = find_level(root.left, value, level+1)
    if left_level != 0:
        return left_level
    return find_level(root.right, value, level+1)
 
def find_distance(root, value1, value2):
    if root is None:
        return 0
    if root.value == value1 or root.value == value2:
        return 0
    left_distance = find_distance(root.left, value1, value2)
    right_distance = find_distance(root.right, value1, value2)
    if left_distance != 0:
        return left_distance+1
    if right_distance != 0:
        return right_distance+1
    level1 = find_level(root, value1, 0)
    level2 = find_level(root, value2, 0)
    return level1 + level2
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
 
print(find_distance(root, 4, 5))