"""
Most of the times, datasets contain missing values. Here we explore different ways to handle missing values.
"""

import pandas as pd

df = pd.read_csv('data/data.csv')

#   first of all check across all columns if there is any missing value.
#   this can be using the below code.
#   it will return column names, with either 'true' for missing values and 'false' for none.
print(df.isna().any())


"""
1. perhaps the most simplest, yet wrong way to handle these are to delete records with missing values.
this may cause rise to many more issues, such as if there are numerous such records, then dataset may not provide expected quality results.
"""

df_1 = df.dropna()          #   drop all records with missing values
print(df_1.isna().any())    #   you can see now that all columns have false for missing value check



"""
2. Another way to handle the missing values is to fill the empty records using the mean, median or mode of the entire column.
This method, however, works for numerical data values' column.
"""
print(f'Without filling: {df}')
df_2 = df.area.fillna(df.area.mean())
print(f'After filling using method 2: {df_2}')
