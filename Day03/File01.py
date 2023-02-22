# Polymorphism
def myAdd(num1, num2):
    return num1+num2
def myAdd(num1, num2=10):
    return num1+num2
print(myAdd(10,12))
print(myAdd(15))