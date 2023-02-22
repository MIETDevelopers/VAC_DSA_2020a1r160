#Find maximum element in a list using recursion.
def max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0])
my_list = [45,43,57,69]
print(max(my_list))