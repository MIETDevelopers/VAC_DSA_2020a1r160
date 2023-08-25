def printNum(n):
    n = n*100
    for i in range(1, n+1):
        print(i/100)
inp = int(input("Enter a number: "))
printNum(inp)