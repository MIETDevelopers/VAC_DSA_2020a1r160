#Use map, reduce to sort a list.
from functools import reduce
lst = [5, 2, 8, 3, 9, 1, 6, 4, 7]
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return list(reduce(lambda x, y: x + y, map(lambda x, y: [x, y] if x < y else [y, x], left, right), []))
sorted_lst = merge_sort(lst)
print(sorted_lst)
