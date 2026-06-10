from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started"
    
toyota = Car()
print(toyota.start_engine())  # Car engine started
honda = Bike()
print(honda.start_engine())   # Bike engine started

