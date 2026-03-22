"""
One of the most important library to get to know of when working on data science, artificial intelligence and machine learning
projects. Perhaps the simplest as well.

Pandas can be used to perform data import and export, data cleaning, data transformation and more.

lets explore some uses of pandas below:
"""

#   import pandas library with alias 'pd', you can use different alias, but 'pd' just sound right. 
import pandas as pd

#   1. Reading data

df = pd.read_csv('data/data.csv')   #   reading csv file. with parameter being the file path and name with extension

"""
pandas can be used to read many types of files such as:
    read_csv:       to read csv file
    read_excel:     to read excel files
    read_json:      to read json files
    read_sql:       to read sql files
    read_spss:      to read a spss file

    and more.
"""


#   2. Provides data structures Series and Data Frames

"""
Series is 1d. You can say a column.
Combination of many columns, to make a 2d structure, results in a data frame.

Data frames may be one the most used 2d structure to handle data conveniently.

Series:
        a   5
        b   6
        c   7

data frame:
        name    phy     chem    maths
        jon     55      66      77
        akram   65      52      85
"""

#   3. Display records

print(df.head())    #   head function displays first 5 rows

print(df.tail())    #   tail function displays last 5 rows

print(df['city'])   #   using square brackets, and column name, displays all values in the column

