"""
Linear Regression using sklearn. Including multi variables for prediction.
"""

import pandas as pd
from sklearn import linear_model


df = pd.read_csv('data/lin_reg_multi.csv')

lin_model = linear_model.LinearRegression()

lin_model.fit(df[['age', 'exp', 'skill']], df.salary)




print(lin_model.predict([[32,6,5]]))