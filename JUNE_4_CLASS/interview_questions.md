# Interview Questions: Functions & Loops (June 4 Class)

This document contains conceptual, theoretical interview questions and answers matching the topics covered in the June 4 class (Python Functions, Loops, control statements, and unpacking).

---

## ❓ Interview Questions & Answers

### 1. Explain the difference between `return` and `print` inside a Python function.
**Answer:**
*   **`print`** is a built-in function that displays output on the console/terminal for debugging or user-viewing purposes. It does not send any data back to the calling expression.
*   **`return`** is a language keyword that terminates the execution of a function and passes a specific value back to the caller. This return value can then be stored in variables, used in mathematical calculations, or passed as arguments to other functions. If a function lacks a `return` statement, it implicitly returns `None`.

---

### 2. What is the difference between a function parameter and a function argument?
**Answer:**
*   A **parameter** is the variable defined in the function's declaration/signature (e.g., `def my_func(parameter_1):`). It acts as a local placeholder for incoming data.
*   An **argument** is the actual value or variable that is passed to the function when it is called (e.g., `my_func("argument_value")`).

---

### 3. Explain how default parameters work in Python. What is the syntax, and what is a common pitfall when using mutable objects (like lists) as default values?
**Answer:**
Default parameters allow you to specify fallback values for parameters that are not supplied during the function call. The syntax is:
```python
def calculate_total(rate, quantity, tax_rate=0.05):
    # tax_rate is optional and defaults to 0.05
    return rate * quantity * (1 + tax_rate)
```
*   **Pitfall:** Python evaluates default parameter values once at the time of function definition, not dynamically upon each execution. If you use a mutable object (e.g., a list or dictionary) as a default parameter, all calls to that function will share the same object in memory, leading to unexpected data persistence across calls.
*   **Solution:** Use `None` as the default value and instantiate the list inside the function:
```python
def append_to_list(element, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(element)
    return target_list
```

---

### 4. Describe the difference between a `for` loop and a `while` loop. When would you prefer one over the other?
**Answer:**
*   **`for` loop:** Used for definite iteration. It loops over a known sequence (like a list, dictionary, tuple, string, or `range`) a pre-determined number of times. You prefer a `for` loop when you know the collection size or iterations beforehand.
*   **`while` loop:** Used for indefinite iteration. It repeatedly runs a block of code as long as a specified condition evaluates to `True`. You prefer a `while` loop when the number of iterations depends on dynamic changes (e.g., reading user input, waiting for a server request, or monitoring a changing game state).

---

### 5. Explain the roles of the `break` and `continue` keywords inside loops. How do they alter the flow of control?
**Answer:**
*   **`break`:** Immediately terminates the loop block completely. The program control flows directly to the first statement situated below the loop.
*   **`continue`:** Skips the rest of the statements in the *current* iteration of the loop and jumps directly to the loop's header to evaluate the next cycle (or condition check).

---

### 6. When looping over a dictionary using a `for` loop, what does the `.items()` method do?
**Answer:**
The `.items()` method returns a view object of key-value pairs as a sequence of tuples (e.g., `dict_items([('key1', 'val1'), ('key2', 'val2')])`). When used in a loop, it enables tuple unpacking so you can bind and access both the key and the value concurrently:
```python
for table, order in order_queue.items():
    print(f"Table {table} ordered {order}")
```
