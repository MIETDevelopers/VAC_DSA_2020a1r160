def separate_and_combine(input_string):
    alphabets = []
    numbers = []
    
    for char in input_string:
        if char.isalpha():
            alphabets.append(char)
        elif char.isdigit():
            numbers.append(int(char))
    
    alphabet_string = ''.join(alphabets)
    
    while len(numbers) > 1:
        new_sum = sum(numbers)
        numbers = [new_sum]

    final_value = numbers[0] if numbers else 0
    
    return alphabet_string, final_value

input_string = input("Enter a string: ")

alphabet_result, final_value_result = separate_and_combine(input_string)

print("Alphabets:", alphabet_result)
print("Sum Value:", final_value_result)
