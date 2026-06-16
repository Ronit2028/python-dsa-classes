#bubble sort
# pass 16,7
# [4,2,7,1,3,6,5]
#[2,4,7,1,3,6,5]
# [2,4,1,7,3,6,5]
# [2,4,1,3,7,6,5]
# [2,4,1,3,6,7,5]
# [2,4,1,3,6,5,7]

# pass 2
# [2,1,4,3,6,5,7]
# [2,1,3,4,6,5,7]
# [2,1,3,4,5,]

#pass 3
# [1,2,3,4,5,6,7]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # last i elements are already in place
        for j in range(0, n-i-1):
            #compare adjacent elements
            if arr[j] > arr[j+1]:
                # swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [11,2,4,8,5,6,7,3,9,10]
sorted_arr = bubble_sort(arr)
print(sorted_arr)