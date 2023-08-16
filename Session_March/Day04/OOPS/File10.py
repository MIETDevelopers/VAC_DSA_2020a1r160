#OOPS: Classes & Objects - Abstraction
from abc import ABC, abstractclassmethod
class square(ABC):
    @abstractclassmethod
    def value(self, a):
        pass
class Main(square):
    def value(self, a):
        return a*a
obj = Main()
print(obj.value(10))