# Call by value/refernces
def myFunc(x):
    x[0]=20
lst = [10, 20, 30, 40]
print(lst)
myFunc(lst)
print(lst)