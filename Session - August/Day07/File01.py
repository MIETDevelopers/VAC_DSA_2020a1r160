def print_beautiful_pattern(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
        
try:
    num_rows = int(input("Enter the number of rows for the pattern: "))
    print_beautiful_pattern(num_rows)
except ValueError:
    print("Please enter a valid number.")