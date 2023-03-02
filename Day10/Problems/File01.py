#create a binary tree for each sublist of a given nested list and root of each node to be used as a graph

def create_binary_trees(nested_list):
   
    if not isinstance(nested_list, list):
        return {}
    
    trees = {}
    
    for sublist in nested_list:
        if isinstance(sublist, list):
            left_sublist = sublist[0] if len(sublist) > 0 else None
            right_sublist = sublist[1] if len(sublist) > 1 else None
            
            left_tree = create_binary_trees(left_sublist)
            right_tree = create_binary_trees(right_sublist)
            
            root = str(sublist)
            
            tree = {'root': root, 'left': left_tree, 'right': right_tree}
            
            trees[root] = tree
    
    return trees
nested_list = [1, [2, [4], [5]], [3, [6], [7]]]
binary_trees = create_binary_trees(nested_list)
print(binary_trees)