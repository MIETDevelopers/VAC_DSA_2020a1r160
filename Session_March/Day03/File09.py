def swap(x,y):
    temp = x
    x = y
    y = temp
    return x, y
x = 10
y = 20
print(x, y)
print(swap(x, y))