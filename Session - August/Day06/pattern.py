#solid
#hollow

# star lower diagonal triangle 
n = int(input("Enter n: "))

for i in range(1, n+1):
    for j in range(0, i):
        print("*", end = "")
    print("")
    
# reverse increasing triangle
n1 = int(input("Enter n1: "))

for i in range(1, n1+1):
    for j in range(n1 - i+1):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# upper left diagonal triangle

n2 = int(input("Enter n2: "))
for i in range(1, n2+1):
    for j in range(n2-i+1):
        print("*", end ="")
    print("")
<<<<<<< HEAD
    
# for lower Left+ lower right triangle

n3 = int((input("Enter n3: ")))


for i in range(1, n3+1):
    for j in range(i):
        print("*", end = " ")
    for j in range(n3-i+1):
        print(" ", end= " ")
    for j in range(n3 -i+1):
        print(" ", end= " ")
    for j in range(i):
        print("*", end = " ")
    print()
=======
>>>>>>> 8e755cb062085a1e7b3e49c93a2c0144cda12d87
