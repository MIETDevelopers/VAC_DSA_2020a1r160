#OOPS: Classes & Objects - Overriding
def add(x,y,z =3):
    return x+y+z
print(add(2,1))
print(add(34,1,4))

class Example:
    def display(self):
        print("Example class")
class Example2(Example):
    def display(self):
        print("Example 2 Class")
    def display(self):
        print("Example 2 second class")
obj = Example2()
obj.display()