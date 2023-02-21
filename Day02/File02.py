#Sets problem
def find_set_intersection(set1, set2, list1):
    set3 = set1.intersection(set2)
    print("Elements from set1 present in set2:", set3)
    set4 = set(list1).difference(set2)
    print("Elements not present in set2:", set4)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 2}
list1 = [2, 3]

find_set_intersection(set1, set2, list1)
