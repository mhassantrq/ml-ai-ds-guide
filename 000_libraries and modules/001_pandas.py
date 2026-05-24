"""
One of the most important library to get to know of when working on data science, artificial intelligence and machine learning
projects. Perhaps the simplest as well.

Pandas can be used to perform data import and export, data cleaning, data transformation and more.

lets explore some uses of pandas below:
"""

#   import pandas library with alias 'pd', you can use different alias, but 'pd' just sound right. 
import pandas as pd

#       1. Reading data

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


#       2. Provides data structures Series and Data Frames

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

#       3. Display records

print(df.head())    #   head function displays first 5 rows

print(df.tail())    #   tail function displays last 5 rows

print(df['city'])   #   using square brackets, and column name, displays all values in the column

#       4. Exploring Data

print(df.info())        # summary information

print(df.describe())    # statistical summary

print(df.shape)         # display total rows and columns

print(df.columns)       # display column names

#       5. Sorting and aggregating data

print(df['area'].sum())         # take sum of 'area' column

print(df['area'].mean())         # take mean of 'area' column

print(df['area'].min())         # take minimum of 'area' column

print(df['area'].max())         # take maximum of 'area' column

print(df.sort_values('area'))         # sort dataframe on 'area' column in ascending order

#       6. handling missing values

print(df.isna())                # display all rows and columns with boolean 'true' indicating if there is any missing value at exact position

print(df.isna().sum())          # showing exactly how many missing values in each column of data frame

print(df['area'].fillna(df['area'].mean()))     # fill every missing value in column 'area' with mean of that respective column

