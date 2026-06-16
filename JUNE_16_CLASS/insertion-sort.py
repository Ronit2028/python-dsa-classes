#insertion sort algorithm

# [11,2,4,8,5,6,7,3,9,10]
#pass 1

#[2,11,4,8,5,6,7,3,9,10]

#pass 2
#[2,4,11,8,5,6,7,3,9,10]

#pass 3
#[2,4,8,11,5,6,7,3,9,10]

#pass 4
#[2,4,5,8,11,6,7,3,9,10]

#pass 5
#[2,4,5,6,8,11,7,3,9,10]

#pass 6
#[2,4,5,6,7,8,11,3,9,10]

#pass 7
#[2,3,4,5,6,7,8,11,9,10]

#pass 8
#[2,3,4,5,6,7,8,9,11,10]

#pass 9
#[2,3,4,5,6,7,8,9,10,11]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i -1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [11,2,4,8,5,6,7,3,9,10]
sorted_arr = insertion_sort(arr) 
print(sorted_arr)  