#OOPS: Classes & Objects - Single level inheritance
class BaseClass:
    name = ''
    age = 0
    def __init__(self):
        name = self.name
        age = self.age
class Derived(BaseClass):
    height = 0
    def __init__(self, name, age, height):
        print(name, age, height)
obj = Derived('Ishav', 19, 165)