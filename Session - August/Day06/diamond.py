def print_diamond_pattern(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "* " * i)
    for i in range(height - 1, 0, -1):
        print(" " * (height - i) + "* " * i)

height = int(input("Enter the height of the diamond: "))
print_diamond_pattern(height)