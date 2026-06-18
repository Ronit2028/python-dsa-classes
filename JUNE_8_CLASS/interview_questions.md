# Interview Questions: Classes, OOP Basics & Encapsulation (June 8 Class)

This document contains conceptual, theoretical interview questions and answers matching the topics covered in the June 8 class (Object-Oriented Programming, `__init__`, `self`, Encapsulation with private attributes, Inheritance, and Method Overriding).

---

## ❓ Interview Questions & Answers

### 1. What is the relationship between a Class and an Object?
**Answer:**
*   A **Class** is a blueprint, template, or abstract definition that specifies what attributes (data) and methods (behaviors) a group of similar objects will share.
*   An **Object** is a concrete instance of a class. It represents a specific entity constructed from the class blueprint, occupying memory and holding individual state values.

---

### 2. What is the purpose of the `__init__` method in Python classes? What does the `self` parameter represent?
**Answer:**
*   **`__init__`** is a special method (often called a dunder method or constructor) that Python automatically executes when a new object of that class is created. Its primary role is to initialize the instance attributes of the new object.
*   **`self`** represents the specific object instance that is currently being created or operated on. By using `self.attribute_name = value`, we ensure the data is saved individually to that specific object, rather than globally across the class.

---

### 3. How does Python implement encapsulation and private attributes? Explain "name mangling."
**Answer:**
*   **Encapsulation** is the practice of bundling data and code together into a single unit (a class) and restricting direct access to the internal details.
*   In Python, prefixing an attribute with two underscores (e.g., `self.__balance`) marks it as **private**, preventing standard external access (e.g., `object.__balance` will throw an `AttributeError`).
*   Python achieves this through **name mangling**. Internally, Python renames `__balance` to `_ClassName__balance`. While this doesn't completely block access if someone intentionally uses the mangled name, it acts as a strong guard against accidental modification and inheritance clashes.

---

### 4. What is Inheritance in OOP? Explain the "IS-A" relationship and how the `super()` function is used.
**Answer:**
*   **Inheritance** allows a child class (subclass) to inherit attributes and methods from a parent class (superclass), promoting code reuse and establishing hierarchies.
*   Inheritance represents an **"IS-A"** relationship. For example, a `Car` *is a* `Vehicle`.
*   **`super()`** is a built-in function that returns a proxy object referencing the parent class. It is commonly used inside a subclass's `__init__` method to invoke the parent class's constructor (`super().__init__(brand)`), ensuring parent class attributes are correctly initialized.

---

### 5. What is Method Overriding? How does it enable polymorphic behavior?
**Answer:**
*   **Method Overriding** occurs when a child class defines a method with the same name and signature as a method already defined in its parent class. The child's implementation replaces the parent's default behavior for that subclass.
*   This enables **polymorphism** ("many forms"). If a program iterates through a list of different objects (e.g., a `Dog` and a `Cat` that inherit from `Animal`) and calls a common method (e.g., `sound()`), each object invokes its overridden version. The caller doesn't need to know the specific subclass type to trigger the appropriate behavior.
