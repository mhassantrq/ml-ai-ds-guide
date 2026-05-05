"""
Decision Tree using sklearn
"""

import pandas as pd
from sklearn import tree


df = pd.read_csv('data/classification01.csv')

#print(df)

dt_model = tree.DecisionTreeClassifier()

dt_model.fit(df[['study', 'attendance', 'assignments']], df.result)

print(dt_model.predict([[1,70,2]]))