#Find maximum of two number using lambda
greater = lambda a,b,c:a if a>b and a>c else b if b>c else c
print(greater(40, 20, 30))