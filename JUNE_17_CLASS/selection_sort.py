arr = [2,10,8,1,4,6,3,5,7,9]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        print(f"Considering subarray: {arr[i:n]}, starting index: {i}, current minimum: {arr[min_index]} at index {min_index}")
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
                print(f"New minimum found: {arr[min_index]} at index {min_index}")
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print("Unsorted array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
