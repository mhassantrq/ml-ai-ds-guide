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
