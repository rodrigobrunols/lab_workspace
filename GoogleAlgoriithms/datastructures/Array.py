# array = []
#
# initializedArray = [0,1,2,3,4,5,6,7,8,9]
#
# array.append(1)
# array.append(10)
#
#
# initializedArray.append(11)
#
# print(array)
#
# print(initializedArray)
#
# initializedArray.remove(9)
#
# print(initializedArray)
#
#
# arr = [1, 2, 3, 4, 5]
# i = 0
# while i < len(arr):
#     print(arr[i])
#     i+=1
#
#
# arr1 = [1, 2, 3]

arr10 = [10, 7, 5]

for i, j in enumerate(arr10):
    print(i, j)

print(enumerate(arr10))

# Define the arrays
array1 = [1, 2, 3]
array2 = ['a', 'b', 'c']

# Iterate over both arrays simultaneously
for i, j in zip(array1, array2):
    print(i, j)

# return max between 2 integer a and b using python native function
print(max(1, 2))  # Output: 2

print()

for i in range(len(arr10)):
    print(i)

print()

for i in range(3):
    print(i)

print()
# for jump in range(0, 10, 2):
for jump in range(0,10, 2):
    print(jump)
