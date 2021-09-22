import numpy as np

narrayOne = np.array([[10, 15, 20], [2, 3, 4], [9, 14.5, 18]])
narrayTwo = np.array([[1, 2, 5], [8, 0, 12], [11, 3, 22]])

# First array

print('Array =:', narrayOne)
print('Array Shape =', narrayOne.shape)
narrayOneSlice = narrayOne[0:2, 0:2]
print('Array Slice = ', narrayOneSlice)

narrayOneTF = narrayOne[narrayOne % 2 == 1]

print('Array True or False =', narrayOneTF)

# Both Arrays

array_sum = narrayOne + narrayTwo
print(array_sum)

array_mult = narrayOne * narrayTwo
print(array_mult)

# Second Array
array2Sum = narrayTwo.sum()
print(array2Sum)

print(narrayTwo.max())

print(narrayTwo.min())

