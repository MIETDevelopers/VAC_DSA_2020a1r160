#solid

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


# pyramid
print("Pyramid")
py = int(input("Enter n:"))
for i in range(1, py + 1):
    for j in range(py-i):
        print(" ", end= " ")
    for j in range(2*i - 1):
        print("*", end=" ")
    print()
        
# reverse pyramid
print("Reverse pyramid")
py1 = int(input("Enter n: "))
for i in range(py1, 0, -1):
    for j in range(py1 - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

# hourglass
print("Hourglass")

py2 = int(input("Enter n: "))
for i in range(py2, 0, -1):
    for j in range(py2 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
    
for i in range(2, py2 + 1):
    for j in range(py2 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()


# diamond

# hollow patterns
#hollow right angled triangle

def print_half_hollow_pattern(height):
    for i in range(1, height + 1):
        if i == 1 or i == height:
            print("* " * i)
        else:
            print("* " + "  " * (i - 2) + "* ")

height = int(input("Enter the height of the pyramid: "))
print_half_hollow_pattern(height)

#hollow pyramid

def print_hollow_pyramid(height):
    for i in range(1, height + 1):
        if i == 1 or i == height:
            print(" " * (height - i) + "* " * i)
        else:
            print(" " * (height - i) + "* " + "  " * (i - 2) + "* ")

height = int(input("Enter the height of the pyramid: "))
print_hollow_pyramid(height)


def hollow_pyramid_alpha(height):
    alphabet = ord('A')
    for i in range(0, height):
        if i == 0:
            print(" " * (height - i - 1) + chr(current_char))
        else:
            spaces = " " * (2 * i - 1)
            print(" " * (height - i - 1) + chr(current_char) + spaces + chr(current_char))
        current_char += 1
 
height = int(input("Enter height: "))
print(hollow_pyramid_alpha(height))           