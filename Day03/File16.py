# Using lambda and map multiply all the values in list with 5
numbers = [6,3,45,6,4,9,1]
multiplied_numbers = list(map(lambda x: x * 5, numbers))
print(multiplied_numbers)