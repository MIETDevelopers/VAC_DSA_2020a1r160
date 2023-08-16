#OOPS: Classes & Objects - Multi level inheritance
class Base:
    def __init__(self, brand):
        self.brand = brand
        print(self.brand)
class Derived(Base):
    def __init__(self, brand, color, model):
        Base.__init__(self, brand)
        self.color = color
        self.model = model
        print(self.color, self.model)
class SubDerived(Derived):
    def __init__(self, brand, color, model, price):
        Derived.__init__(self, brand, color, model)
        self.price = price
        print(self.price)
class Main:
    obj = SubDerived('Jeep', 'Black', 'Compass', 2100000)