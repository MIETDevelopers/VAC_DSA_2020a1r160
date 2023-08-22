def pattern_print(n):
    for i in range(1, n+1):
        print("*" * i + " " * ((n*2)-(i*2)) + "*" * (i))
n = int(input("Enter n: "))
pattern_print(n)