# Try Catch in functions.
def operation(*args):
    x,y = args
    if y == 0:
        b = x/y
        print(b)
    print(b+x+y)
try:
    operation(10,2)
except ZeroDivisionError:
    print('ZeroDivisionError Occured')
except NameError:
    print('NameError Occured.')
else:
    print('No Error')