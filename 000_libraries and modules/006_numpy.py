"""
Used for numerical computing, scientific analysis. Fasters, basis for many libraries. Used for many purposes in ai, ml and ds.
"""
import numpy as np


#   create an array using values
arr = np.array([1,2,3,4])
print(f'Array of numbers: {arr}')

#   create an array of numbers with range and jump size
arr = np.arange(3, 10, 2)
print(f'Array of numbers in range given jump size: {arr}')

#   create an array of numbers given range and total values
arr = np.linspace(0, 10, 20)
print(f'Array of numbers in range given total values of equal space: {arr}')

#   create an array of zeros with given dimensions
arr = np.zeros((3,5))
print(f'Array of zeros of dimension 3,5: {arr}')

#   create an array of ones with given dimensions
arr = np.ones((3,5))
print(f'Array of ones of dimension 3,5: {arr}')

#   output dimension of array
print(f'Dimension of array: {arr.ndim}')

#   output shape of array
print(f'Shape of array: {arr.shape}')

#   output size of array
print(f'Size of array: {arr.size}')

#   output data type of array
print(f'Data type of array: {arr.dtype}')

#   array slice
print(f'array: {arr[1:2, 0:1]}')    #   row from 1 to 2 and columns from 0 to 1
print(f'array: {arr[:, 0:1]}')    #   all rows and columns from 0 to 1
print(f'array: {arr[1:2, :]}')    #   row from 1 to 2 and all columns
print(f'array: {arr[:, :]}')    #   all rows and all columns

arr = np.array([
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [3, 5, 7, 9]
])

print(f'{arr}')

#   reshape array
print(f'reshaped array: {arr.reshape(6,2)}')

#   flatten array
print(f'reshaped array: {arr.flatten()}')   #   flatten to one dimensional array