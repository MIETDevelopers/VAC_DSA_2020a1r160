#Find the sum of digits of a given number
def sum(num):
    if num == 0:
        return 0
    else:
        return int(num%10 + sum(num//10))
out = sum(12345)
print(out)