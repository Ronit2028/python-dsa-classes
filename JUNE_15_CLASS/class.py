# =====================================================================
# Understanding Time Complexity & Big-O Notation
# For detailed theoretical explanations, see:
# [time complexity.md](file:///Users/ronitjaipraash/Desktop/Github%20Sessions/python-dsa-classes/JUNE_15_CLASS/time%20complexity.md)
# =====================================================================

# 1. Constant Time: O(1)
# Execution time remains constant, regardless of the input size (N).
def constant_time_demo(arr):
    # Accessing an element by index takes exactly 1 step
    if len(arr) > 0:
        return arr[0]
    return None

# 2. Linear Time: O(N)
# Execution time grows proportionally to the input size (N).
def linear_time_demo(arr):
    # Traverses the list once. N operations for N elements.
    for element in arr:
        pass  # Process element

# 3. Quadratic Time: O(N^2)
# Execution time grows proportionally to the square of input size (N).
# Usually represented by nested loops over the same input.
def quadratic_time_demo(arr2d):
    # Nested loops to traverse a 2D grid/array.
    n = len(arr2d)
    for i in range(n):
        for j in range(len(arr2d[i])):
            # If arr2d is N x N, this executes N * N times
            _ = arr2d[i][j]

# 4. Logarithmic Time: O(log N)
# Execution time increases by 1 step every time the input size doubles.
# Commonly seen in divide-and-conquer loops where search space is halved.
def logarithmic_time_demo(n):
    steps = 0
    while n > 1:
        n = n / 2
        steps += 1
    return steps

# =====================================================================
# Big-O Simplification Rules
# =====================================================================
# Rule 1: Drop constant factors (ignoring scaling multipliers)
# e.g., 2n + 5  ==> O(n)
# e.g., 2n      ==> O(n)

# Rule 2: Keep the dominant term (ignore lower order terms)
# e.g., 5n^2 + n + 2  ==> O(n^2) because n^2 grows much faster than n

if __name__ == "__main__":
    # Test Data
    test_arr = [1, 2, 6, 4, 5, 3]
    test_arr_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    print("O(1) Constant element access:", constant_time_demo(test_arr))
    print("O(log N) Logarithmic steps for n=64:", logarithmic_time_demo(64))


