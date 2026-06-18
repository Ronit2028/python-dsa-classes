# Interview Questions: Abstraction, Polymorphism & Getters/Setters (June 10 Class)

This document contains conceptual, theoretical interview questions and answers matching the topics covered in the June 10 class (Abstract Classes, ABC, `@abstractmethod`, Polymorphism, Getters and Setters, and Class hierarchies).

---

## ❓ Interview Questions & Answers

### 1. What is the difference between a normal class and an abstract class in Python?
**Answer:**
*   A **normal class** is a fully implemented class that can be instantiated directly (e.g., `obj = MyClass()`). It can contain regular attributes and methods.
*   An **abstract class** is a class that inherits from the `abc.ABC` module and contains one or more abstract methods (methods declared but not fully implemented). Abstract classes **cannot be instantiated** directly; they serve as templates for child classes to inherit from and implement.

---

### 2. What is an abstract method, and how do you define one in Python?
**Answer:**
*   An **abstract method** is a method that is declared in a parent class but lacks a concrete implementation (the body usually consists of just `pass`).
*   It serves as a contract, forcing any subclass to implement this method before it can be instantiated.
*   In Python, you import `ABC` and `abstractmethod` from the `abc` module and decorate the method using `@abstractmethod`:
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
```

---

### 3. What is Polymorphism in OOP? How does it relate to inheritance and method overriding?
**Answer:**
*   **Polymorphism** means "having many forms." It allows different objects to respond to the exact same method call in their own unique ways.
*   It relies on **inheritance** to ensure that subclasses share a common interface or parent class.
*   It relies on **method overriding** to allow each subclass to replace the parent class's method with its own specific implementation. For instance, calling `.area()` on instances of `Circle` or `Square` executes different mathematical logic, but the caller uses the same method name.

---

### 4. Why does Python throw a `TypeError` if you try to instantiate an abstract class or a child class that has missed implementing an abstract method?
**Answer:**
*   An abstract class is intentionally incomplete. Instantiating it directly would create objects with undefined behaviors (calling a method that only has `pass` inside the abstract class).
*   If a child class inherits from an abstract class but fails to override even one abstract method, it remains abstract. Python raises a `TypeError` upon instantiation to protect the program from invoking un-implemented methods at runtime.

---

### 5. What is the purpose of Getter and Setter methods? Why are they useful for Encapsulation?
**Answer:**
Getters and Setters provide controlled access to private attributes:
*   **Getter (Access Method):** A public method used to retrieve the value of a private variable safely (e.g., `get_value()`).
*   **Setter (Mutator Method):** A public method used to modify the value of a private variable (e.g., `set_value(new_val)`).
*   **Encapsulation Benefits:**
    1.  **Validation:** Setters allow you to filter inputs (e.g., preventing a user from setting `balance` to a negative number).
    2.  **Read-Only attributes:** By providing a getter but no setter, you can make an attribute read-only.
    3.  **Abstraction:** You can change the internal data structure without breaking external code that relies on the getter/setter interface.
