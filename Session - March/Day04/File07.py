# Try Catch in functions.
def operation(*args):
    x,y = args
    if y == 0:
        raise ZeroDivisionError()
    else:
        print(x+y)
try:
    operation(10,0)
except:
    print('Some error was thrown.')
finally:
    print('Execution Done')