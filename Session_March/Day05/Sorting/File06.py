#Insertion sort using Recursion.
lst = [4,5,3,2,6,1]
def insertion_sort(lst, n):
    if n <= 1:
        return
    insertion_sort(lst, n-1)
    last = lst[n-1]
    j = n-2
    while (j >= 0 and lst[j] > last):
        lst[j+1] = lst[j]
        j -= 1
    lst[j+1] = last
    return lst

print(insertion_sort(lst, len(lst)))