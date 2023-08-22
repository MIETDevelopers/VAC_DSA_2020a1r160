def print_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)
def print_pattern2(n):
    for i in range(n):
        print("*" * (n-i))

n = int(input("Enter the number of rows: "))
print_pattern(n)
print("------------")
print_pattern2(n)