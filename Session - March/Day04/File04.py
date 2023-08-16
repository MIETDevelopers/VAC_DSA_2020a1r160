# Try Catch in functions.
def operation(*args):
    x,y = args
    if y == 0:
        print(x/y)
    else:
        print(x+y)
try:
    operation(10,0)
except:
    print('Some error was thrown.')
operation(10,5)