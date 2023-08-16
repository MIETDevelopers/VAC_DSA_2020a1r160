#OOPS: Classes & Objects - Encapsulation
class Details:
    def __init__(self):
        print('Class Details')
        self.a = 10
        self._b = 20
        self.__c = 30

    def get_c(self):
        return self.__c

class Print(Details):
    def __init__(self):
        Details.__init__(self)
        print(self.a, self._b)

obj1 = Print()
print(obj1.get_c())