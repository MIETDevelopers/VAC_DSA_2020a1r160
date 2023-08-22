for i in range(0, height):
        if i == 0:
            print(" " * (height - i - 1) + chr(current_char))
        else:
            spaces = " " * (2 * i - 1)
            print(" " * (height - i - 1) + chr(current_char) + spaces + chr(current_char))
        current_char += 1