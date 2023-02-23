my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

try:
    n = int(input())
    if n < 0 or n > 9:
        raise IndexError
    print(my_list[n])
except ValueError:
    print("Invalid input!")
except IndexError:
    print("Index out of range!")
