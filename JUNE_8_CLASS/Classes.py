# CLASS — The Blueprint
class House:
    def __init__(x, color, rooms):
        x.color = color
        x.rooms = rooms

    def describe(x):
        return f"A {x.color} house"
    

my_house = House("blue", 3)
your_house = House("red", 5)

# Each object is unique!
print(my_house.color)    # blue
print(your_house.rooms)  # 5

print(your_house.describe())  # A red house



class Dog:
    def __init__(self, name, breed):
        # 'self' = reference to this object
        self.name = name    # instance attr
        self.breed = breed  # instance attr

    def bark(self):
        return f"{self.name}: Woof!"

rex = Dog("Rex", "Husky")
buddy = Dog("Buddy", "Lab")
print(rex.bark())    # Rex: Woof!
print(buddy.bark())  # Buddy: Woof!


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def get_balance(self):       # getter
        return self.__balance

    def deposit(self, amount):   # setter
        if amount > 0:
            self.__balance += amount

acct = BankAccount(1000)
print(acct.get_balance())  # 1000
acct.deposit(500)   
print(acct.get_balance())  # 1500        



class Vehicle:            # Parent class
    def __init__(self, brand):
        self.brand = brand
    def move(self):
        return f"{self.brand} moves"

class Car(Vehicle):       # Car IS-A Vehicle
    def __init__(self, brand, doors):
        super().__init__(brand)   # inherit
        self.doors = doors

car = Car("Toyota", 4)
print(car.move()) # Toyota moves
print(car.doors) # 4




class Animal:
    def sound(self):
        return "..."

class Dog(Animal):
    a = 1

class Cat(Animal):
    def sound(self):      # Override
        return "Meow!"

# One interface — many behaviours
for animal in [Dog(), Cat()]:
    print(animal.sound())