def partition(arr, low, high):
    # Select the rightmost element as the pivot
    pivot = arr[high]
    i = low - 1  # Index of the smaller element
    
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    # Place pivot in its correct sorted position by swapping with element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
        
    # Base Case: recurse only if there is more than 1 element to sort
    if low < high:
        # Partition the array and retrieve the pivot's final index
        pivot_index = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
        
    return arr


# --- Execution Example ---
if __name__ == "__main__":
    test_arr = [24, 9, 29, 14, 19, 27]
    print("Unsorted Array:", test_arr)
    
    sorted_arr = quick_sort(test_arr)
    print("Sorted Array:  ", sorted_arr)
