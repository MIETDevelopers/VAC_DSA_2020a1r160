# Variable length, non keyword.
def func1(*args):
    for i in args:
        print(i)
func1("Ishav", 1, "Hello")