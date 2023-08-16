# Using reduce to find the maximum element in the list
from functools import reduce
numbers = [10, 51, 29, 34, 39, 69]
print(reduce(lambda a, b: a if a > b else b, numbers))