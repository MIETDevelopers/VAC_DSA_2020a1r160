#OOPS: Classes & Objects - Multiple inheritance
class Base1:
    def __init__(self):
        self.str1 = 'Parent 1'
        print('Base 1')
class Base2:
    def __init__(self):
        self.str2 = 'Parent 2'
        print('Base 2')
class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print('Child')
    def display(self):
        print(self.str1, self.str2)
obj = Derived()
obj.display()