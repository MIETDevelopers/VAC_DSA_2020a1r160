# format string --- add spaces
def format_string(input_string):
    formatted_string = ""
    i = 0
    while i < len(input_string):
        if input_string[i].isupper() and i > 0:
            formatted_string += " "
        formatted_string += input_string[i].lower()
        i += 1
    return formatted_string

input_string = "ThePairOfShoeCostedSomeBucks"
print(format_string(input_string))