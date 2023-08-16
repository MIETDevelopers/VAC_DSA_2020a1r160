#map fucntion
def add(n):
    return n+n
numbers = [1,2,3,4]
result = map(add, numbers)
print(list(result))