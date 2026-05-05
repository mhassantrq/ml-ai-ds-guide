"""
Decision Tree using sklearn
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

df = pd.read_csv('data/classification01.csv')

#print(df)

dt_model = DecisionTreeClassifier()

dt_model.fit(df[['study', 'attendance', 'assignments']], df.result)

print(dt_model.predict([[1,70,2]]))


"""
Decision Plot Tree

plt.figure(figsize=(10,6))
plot_tree(dt_model, feature_names=df[['study', 'attendance', 'assignments']].columns, filled=True)
plt.show()
"""
