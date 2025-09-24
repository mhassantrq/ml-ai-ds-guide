"""
Dataset can be loaded in various ways. Lets explore them below one by one:
"""

# 1. Using pandas


import pandas as pd

#   read csv file using pandas
df = pd.read_csv('data/data.csv')

#   print the data frame to view the file data
print(df)