#Bubble sort in python
def bubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
lst = [5,2,1,3,4,6]
print(bubbleSort(lst))