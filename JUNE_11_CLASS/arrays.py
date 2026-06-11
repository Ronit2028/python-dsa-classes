array = []
print(array)

# inital values 
array_1 = [1, 2, 3, 4, 5]
print(array_1)

# using list comprehension to create an array of squares of numbers from 1 to 5
array_2 = [x*2 for x in range(1, 6)]
print(array_2)

# using range to create an array of numbers from 1 to 10
array_3 = list(range(1, 11))
print(array_3)

# for repeatation of values
array_4 = [0] * 5
print(array_4)


print(array_3[0])  # accessing the first element
print(array_3[4])  # accessing the fifth element
print(array_3[-1]) # accessing the last element

print(array_3[-3::2])  # accessing the first five elements with a step of 2