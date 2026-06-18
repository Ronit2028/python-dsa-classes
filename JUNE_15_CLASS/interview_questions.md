# Interview Questions: Binary Search & Array Operations (June 15 Class)

This document contains conceptual, theoretical interview questions and answers matching the topics covered in the June 15 class (Binary Search, list insertion, deletion, appending, and search complexity).

---

## ❓ Interview Questions & Answers

### 1. Under what condition can Binary Search be applied to an array? What is its time complexity?
**Answer:**
*   **Condition:** Binary Search can **only** be performed on arrays that are already **sorted** (either in ascending or descending order). If the array is unsorted, the comparison logic breaks, and it cannot correctly determine which half of the array to discard.
*   **Time Complexity:**
    *   **Best Case:** $\mathcal{O}(1)$ (when the target is found at the first `mid` index check).
    *   **Worst/Average Case:** $\mathcal{O}(\log N)$ (since the search space is divided in half during each iteration).

---

### 2. Compare the efficiency of Linear Search vs. Binary Search for an array of size $N$.
**Answer:**
*   **Linear Search:**
    *   Iterates sequentially from the first element to the last element.
    *   Works on both sorted and unsorted arrays.
    *   Worst-case time complexity is $\mathcal{O}(N)$ (linear).
*   **Binary Search:**
    *   Repeatedly divides the search space in half.
    *   Requires the array to be sorted.
    *   Worst-case time complexity is $\mathcal{O}(\log N)$ (logarithmic).
*   **Efficiency:** For a small array (e.g., $N = 10$), both are extremely fast. However, as $N$ scales to large sizes (e.g., $N = 1,000,000$), Linear Search can take up to $1,000,000$ operations, while Binary Search takes at most $\approx 20$ comparisons, making it exponentially faster.

---

### 3. Explain how pointers `left`, `right`, and `mid` are updated in Binary Search when the target value is greater than the middle element.
**Answer:**
If the target is greater than the middle element (`target > arr[mid]`) in an ascending-sorted array:
*   We know the target cannot reside in the left half, nor can it be the middle element.
*   Therefore, we discard the left half by updating the **`left`** pointer to **`mid + 1`**.
*   The **`right`** pointer remains unchanged.
*   In the next iteration, a new **`mid`** is computed as:
    $$\text{mid} = \frac{\text{left} + \text{right}}{2}$$
    focusing the search strictly on the remaining right half.

---

### 4. What are the time complexities of the following basic array/list operations in Python?
*   Accessing an element by index (e.g., `arr[1]`)
*   Appending an element to the end of the list (e.g., `arr.append(12)`)
*   Inserting an element at index 1 (e.g., `arr.insert(1, 100)`)
*   **Answer:**
    *   **Accessing by index:** $\mathcal{O}(1)$ (Constant Time) because of contiguous memory.
    *   **Appending to the end:** $\mathcal{O}(1)$ (Amortized Constant Time) because Python lists over-allocate memory to accommodate new elements without resizing on every append.
    *   **Inserting at index 1:** $\mathcal{O}(N)$ (Linear Time) because inserting an element at any location except the end requires shifting all subsequent elements one position to the right to make space.

---

### 5. Explain the difference between Python list operations `remove(value)` and `pop()`. What are their respective time complexities?
**Answer:**
*   **`remove(value)`:**
    *   Searches for the first occurrence of a specific value in the list and deletes it.
    *   **Time Complexity:** $\mathcal{O}(N)$ because it must perform a linear search to locate the value first, and then shift all elements behind it to close the gap.
*   **`pop()`:**
    *   Removes and returns the last element of the list.
    *   **Time Complexity:** $\mathcal{O}(1)$ because it accesses the last element directly and requires no element shifting.
    *   *(Note: Calling `pop(i)` with a specific index has a complexity of $\mathcal{O}(N)$ due to element shifting).*
