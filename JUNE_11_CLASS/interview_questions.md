# Interview Questions: Arrays & Lists, Slicing & Indexing (June 11 Class)

This document contains conceptual, theoretical interview questions and answers matching the topics covered in the June 11 class (Python Lists as Arrays, indexing, slicing, range creation, and memory layout).

---

## ❓ Interview Questions & Answers

### 1. In Python, lists are commonly used to represent arrays. What is the time complexity of accessing an element in an array by its index? Why?
**Answer:**
*   Accessing an array element by its index is **$\mathcal{O}(1)$ (Constant Time)**.
*   **Why:** Array elements are stored in contiguous (sequential) blocks of memory. Because the compiler or interpreter knows the start address of the array (the base address) and the size of each element, it can compute the exact physical address of any index instantly using a simple mathematical formula:
    $$\text{Address} = \text{Base Address} + (\text{Index} \times \text{Size of element})$$
    Since this calculation takes a constant number of CPU cycles, access time does not change as the array grows.

---

### 2. Explain Python's negative indexing. What do `arr[-1]` and `arr[-3]` refer to?
**Answer:**
*   Negative indexing allows you to access elements from the end of a list in reverse order, rather than the beginning.
*   `arr[-1]` refers to the very last element of the list.
*   `arr[-3]` refers to the third-to-last element of the list.
*   Internally, `arr[-i]` is evaluated as `arr[len(arr) - i]`.

---

### 3. Explain how list slicing works in Python. What is the meaning of the syntax `arr[start:stop:step]`?
**Answer:**
Slicing creates a new list containing a subset of the original list's elements.
*   `start`: The index where the slice begins (inclusive). If omitted, it defaults to `0` (or the end if step is negative).
*   `stop`: The index where the slice ends (exclusive). If omitted, it defaults to the end of the list (or start if step is negative).
*   `step`: The step size (increment) between items in the slice. If omitted, it defaults to `1`.
*   *Example:* If `arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, then `arr[-3::2]` means: start from the third-to-last element (`8`) and take every second element until the end of the list, producing `[8, 10]`.

---

### 4. Explain the memory difference between a Python list and a traditional primitive array (like in C/C++ or Java).
**Answer:**
*   **Traditional Primitive Array:** Stores values of the exact same data type (homogeneous) sequentially in contiguous memory blocks. The array elements contain the raw data values directly.
*   **Python List:** Is a dynamic array of **object references (pointers)**. Instead of storing values directly, the contiguous memory block stores 64-bit memory addresses that point to objects elsewhere in heap memory. This pointer-based approach allows Python lists to hold heterogeneous (mixed) data types but introduces slight overhead due to pointer dereferencing and extra memory allocation.

---

### 5. What does the syntax `arr = [0] * 5` do in Python? How does it behave in memory?
**Answer:**
*   This syntax creates a list of 5 elements, all initialized to `0` (i.e., `[0, 0, 0, 0, 0]`).
*   **Memory Behavior:** Since integers in Python are objects, Python optimizes this operation. Instead of creating five different integer objects in memory, it creates a list containing five pointer references, all pointing to the *same* immutable integer object `0` in memory. If you change an element (e.g., `arr[0] = 1`), Python simply updates that pointer to point to a new integer object `1`.
*   *Caution:* If you use this syntax with mutable objects (e.g., `[[0]] * 5`), all elements will point to the *same* nested list object, and modifying one nested list will modify all of them.
