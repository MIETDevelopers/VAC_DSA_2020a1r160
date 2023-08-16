#OOPS: Classes & Objects - Hierarchical inheritance
class Base:
    def __init__(self, height):
        self.height = height
        print(height)
class Derived1(Base):
    def __init__(self, name, age, height):
        Base.__init__(self, height)
        print(name, age)
class Derived2(Base):
    def __init__(self, name, age, height):
        Base.__init__(self, height)
        print(name, age)
obj1 = Derived1('Ishav', 20, 170)
obj2 = Derived2('Tanmay', 25, 176)