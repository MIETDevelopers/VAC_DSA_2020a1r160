def print_pyramid(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "* " * i)

height = int(input("Enter the height of the pyramid: "))
print_pyramid(height)