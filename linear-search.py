def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target: 
            print("Element found at index:", i)
            return i 
        else:
            print("Element not found at index:", i) 

arr = [11,2,4,8,5,6,7,3,9,10]
target = 5
linear_search(arr, target)
    

       