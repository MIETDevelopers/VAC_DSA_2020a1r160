# Filter fucntion
def func(value1):
    letters=['a', 'e', 'i', 'o', 'u']
    if (value1 in letters):
        return True
    else:
        return False
sequence = list("tofhgjhfietffyuyatfyu")
filtered = filter(func, sequence)
for i in filtered:
    print(i)