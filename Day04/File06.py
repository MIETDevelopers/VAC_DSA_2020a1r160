# Finnaly : try except
try:
    x = 10
    print(x/0)
except ZeroDivisionError:
    print('Error Occured')
finally:
    print('Execution done.')