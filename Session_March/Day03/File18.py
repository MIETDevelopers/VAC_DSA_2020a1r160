#Reduce method
import functools
lst = [1,2,3,4,5]
print(functools.reduce(lambda a,b:a+b, lst))