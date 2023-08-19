#find nth catalan number
def catalan(n):
    if n<=1:
        return 1
    res=0
    for i in range(n):
        res+=catalan(i)*catalan(n-i-1)
    return res
n=int(input("Value: "))
print(catalan(n))