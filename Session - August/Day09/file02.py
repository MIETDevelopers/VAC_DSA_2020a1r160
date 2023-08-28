def printNum(n):
    n = n*1000
    for i in range(1, n+1):
        print(i/1000)
inp = int(input("Enter a number: "))
printNum(inp)