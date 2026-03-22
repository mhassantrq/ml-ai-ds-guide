"""
Dataset can be loaded in various ways. Lets explore them one by one.
"""

# 1. Using pandas

import pandas as pd

#   read csv file using pandas
df = pd.read_csv('data/data.csv')

#   print the data frame to view the file data
print(df)

"""
pandas can be used to read many types of files such as:
    read_csv:       to read csv file
    read_excel:     to read excel files
    read_json:      to read json files
    read_sql:       to read sql files
    read_spss:      to read a spss file

    and more.
"""


# 2. Using csv library

import csv

with open('data/data.csv', newline='') as f:
    r = csv.reader(f)
    for row in r:
        print(row)


# 3. using python own read files

with open('data/data.csv') as f:
    file = f.read()
print(file)