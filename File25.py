# Sort a list using recusrion
my_list = [11, 20, 1, 30, 24, 1, 22, 6, 7]
def recursive_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        return recursive_sort([x for x in lst[1:] if x < pivot]) + [pivot] + recursive_sort([x for x in lst[1:] if x >= pivot])
sorted_list = recursive_sort(my_list)
print(sorted_list)