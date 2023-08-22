def print_alphabet_pyramid(height):
    current_char = ord('A')
    for i in range(0, height):
        if i == 0:
            print(" " * (height - i - 1) + chr(current_char))
        else:
            spaces = " " * (2 * i - 1)
            print(" " * (height - i - 1) + chr(current_char) + spaces + chr(current_char))
        current_char += 1

height = int(input("Enter the height of the alphabet pyramid: "))
print_alphabet_pyramid(height)