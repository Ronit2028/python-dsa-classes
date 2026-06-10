

# making a class
class MyClass:
    className = "MyClass"
    def sayHello(self, name):
        print(f"Hello, {name}!, I am {self.className}.")

obj = MyClass()
obj.sayHello("Ronit") 
print(type(obj.sayHello("Ronit") )) # Hello, Alice!, I am MyClass.

# class with methods
class Calculator:
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y    
    def multiply(self, x, y):
        product = x * y
        return product        
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"
        
calc = Calculator()
print(calc.add(5, 3))       # 8
print(calc.subtract(5, 3))  # 2
print(calc.multiply(5, 3))
print(type(calc.multiply(5, 3)))  # 15
print(calc.divide(5, 3))    # 1.6666666666666667
print(calc.divide(5, 0))    # Cannot divide by zero


class Student:
    def __init__(self, name, grade, admissionNumber):
        self.name = name
        self.grade = grade
        self.admissionNumber = admissionNumber

    def is_passing(self):
        return self.grade >= 60
    
    def details(self):
        return f"{self.name} (Admission Number: {self.admissionNumber}) has a grade of {self.grade}"
    
student1 = Student("Ronit", 0, "2021BTCS106")
student2 = Student("Alice", 85, "2021BTCS107")  
print(student1.is_passing())  # False
print(student2.is_passing())  # True

print(student1.details())  # Ronit (Admission Number: 2021BTCS106) has a grade of 0
print(student2.details())  # Alice (Admission Number: 2021BTCS107)


class encapsulationDemo:
    def __init__(self, value):
        self.__private_value = value  # private attribute

    def get_value(self):  # getter method
        return self.__private_value

    def set_value(self, new_value):  # setter method
        if new_value >= 0:
            self.__private_value = new_value

demo = encapsulationDemo(10)
print(demo.get_value())  # 10
demo.set_value(20)
print(demo.get_value())  # 20


class areaCalulator:
    def areaOfCircle(self, r):
        area=  3.14 * r ** 2
        return area
    def areaOfRectangle(self, l, b):
        area = l * b
        return area
    

calc = areaCalulator()
print(calc.areaOfCircle(5))  # 78.5


class shapes:
    def area (self, l, b):
        return l * b
    
# class rectangle(shapes):
#     def area(self, l, b):
#         return (l*b)  # Call parent method

class square(shapes):
    def area(self, s):
        return s ** 2

class circle(shapes):
    def area(self, r):
        return 3.14 * r ** 2
    
squ = square()
print(squ.area(4))  # 16
circ = circle()     
print(circ.area(5))  # 78.5

