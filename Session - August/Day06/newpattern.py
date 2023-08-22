# def print_pyramid(height):
#     for i in range(1, height + 1):
#         print(" " * (height - i) + "* " * i)

# height = int(input("Enter the height of the pyramid: "))
# print_pyramid(height)


# # reverse pyramid

# def print_reverse_pyramid(height):
#     for i in range(height, 0, -1):
#         print(" " * (height - i) + "* " * i)

# height = int(input("Enter the height of the pyramid: "))
# print_reverse_pyramid(height)


# #hour glass

# def print_hour_glass(height):
#     for i in range(height, 0, -1):
#         print(" " * (height - i) + "* " * i)
#     for i in range(1, height + 1):
#         print(" " * (height - i) + "* " * i)

# height = int(input("Enter the height of the pyramid: "))
# print_hour_glass(height)

#print diamond

def print_diamond(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "* " * i)
    for i in range(height - 1, 0, -1):
        print(" " * (height - i) + "* " * i)

height = int(input("Enter the height of the pyramid: "))
print_diamond(height)

# half hollow pattern

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
