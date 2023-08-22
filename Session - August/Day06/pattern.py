#solid
#hollow

# star lower diagonal triangle 
n = int(input("Enter n: "))

for i in range(1, n+1):
    for j in range(0, i):
        print("*", end = "")
    print("\n")