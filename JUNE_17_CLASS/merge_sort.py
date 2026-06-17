arr1 = [11,7,13,2,5,9,10,4]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        
        #division of array into halves
        
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        print(left_half)
        print(right_half)
        #recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)
        
        #iterators for traversing the two halves and main list
        i = j = k = 0
        
        #copy of the data to temp arrays left half and right half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            
        #checking if any element was left in left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            
        #checking if any element was left in right half
        while j < len(right_half):  
            arr[k] = right_half[j]
            j += 1
            k += 1    
    
(merge_sort(arr1))
print(arr1)