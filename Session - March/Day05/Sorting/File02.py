#Selection sort using recusrion in python.
def selectionSort(lst):
    if len(lst) <= 1:
        return lst
    else:
        min_index = 0
        for i in range(1, len(lst)):
            if lst[i] < lst[min_index]:
                min_index = i
        lst[0], lst[min_index] = lst[min_index], lst[0]
        return [lst[0]] + selectionSort(lst[1:])
lst = [5,2,1,3,4,6]
print(selectionSort(lst))