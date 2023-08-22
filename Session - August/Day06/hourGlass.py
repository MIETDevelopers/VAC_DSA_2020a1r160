def print_reverse_pyramid(height):
    for i in range(height, 0, -1):
        print(" " * (height - i) + "* " * i)

def print_pyramid(height):
    for i in range(2, height + 1):
        print(" " * (height - i) + "* " * i)

height = int(input("Enter the height of the hourglass: "))
print_reverse_pyramid(height)
print_pyramid(height)