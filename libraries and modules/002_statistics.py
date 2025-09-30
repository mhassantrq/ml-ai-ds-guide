"""
Statistics module
"""

import statistics
import random


data = [random.randint(10, 100) for _ in range(15)]

print(f'data: {data}')


#   Mean
data_mean = statistics.mean(data)
print(f'Mean of data: {data_mean}')


#   Median
data_median = statistics.median(data)
print(f'Median of data: {data_median}')


#   Mode
data_mode = statistics.mode(data)
print(f'Mode of data: {data_mode}')


#   Variance
data_var = statistics.variance(data)
print(f'Variance of data: {data_var}')


#   Standard Deviation
data_std_dev = statistics.stdev(data)
print(f'Standard Deviation of data: {data_std_dev}')


#   Quantiles
data_quantiles = statistics.quantiles(data, n=4)
print(f'Quantiles of data: {data_quantiles}')


