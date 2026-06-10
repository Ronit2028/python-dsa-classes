from abc import ABC, abstractmethod

class Shape(ABC):         # Abstract class
    @abstractmethod
    def area(self):       # Contract
        pass              # Must implement!

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2

c = Circle(5)
print(c.area())           # 78.5


class test:
    @staticmethod
    def add(x, y):
        return x + y
    
print(test.add(3, 4))  # 7