def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            print("Element found at index:", mid)
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


sorted_arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
target = 5
result = binary_search(sorted_arr, target)


