"""
Dataset can be loaded in various ways. Lets explore them.
"""

# 1. Using pandas

import pandas as pd

#   read csv file using pandas
df = pd.read_csv('data/data.csv')

#   print the data frame to view the file data
print(df)

#   for various other input files using pandas see pandas file in libraries and modules directory


# 2. Using csv

import csv

with open('data/data.csv', newline='') as f:
    r = csv.reader(f)
    for row in r:
        print(row)