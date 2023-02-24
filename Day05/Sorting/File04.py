#Bubble sort using Recursion
lst = [5,2,1,3,4,6]
n = len(lst)
def bubbleSort(lst, n):
    if n == 1:
        return lst
    for i in range(n-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    return bubbleSort(lst, n-1)

print(bubbleSort(lst, n))