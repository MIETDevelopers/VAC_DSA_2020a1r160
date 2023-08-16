# Try catch exception.
try:
    x = 10
    print(x/0)
except ZeroDivisionError:
    print('Error Occured')