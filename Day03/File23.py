#Recursion
def sum(n):
    return n + sum(n+1) #recursive call
sum(5)