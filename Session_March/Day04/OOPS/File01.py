#OOPS: Classes & Objects
class Base:
    def __init__(self):
        print('Base Class')
class Derived(Base):
    def __init__(self):
        print('Derived Class')
class Main:
    obj1 = Base()
    obj2 = Derived()