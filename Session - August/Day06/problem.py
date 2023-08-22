def deci_to_bcd(n):
    if n==0:
        return 0
    else:
        return (n%2)+10*deci_to_bcd(n//2)
    
def bcd_to_deci(n):
    if n==0:
        return 0
    else:
        return (n%10)+2*bcd_to_deci(n//10)

n=int(input("Enter a number: "))
print(deci_to_bcd(n))
n1=int(input("Enter a number: "))
print(bcd_to_deci(n1))