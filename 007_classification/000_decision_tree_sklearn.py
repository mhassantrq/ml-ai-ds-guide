"""
Decision Tree using sklearn
1. Decision Tree
2. Extra Tree
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree, ExtraTreeClassifier
import matplotlib.pyplot as plt

df = pd.read_csv('data/classification01.csv')

#   1. Decision Tree
dt_model = DecisionTreeClassifier()
dt_model.fit(df[['study', 'attendance', 'assignments']], df.result)

print(dt_model.predict([[1,70,2]]))


#   2. Extra Tree
et_model = ExtraTreeClassifier()
et_model.fit(df[['study', 'attendance', 'assignments']], df.result)

print(et_model.predict([[5,85,6]]))


"""
Decision Plot Tree

plt.figure(figsize=(10,6))
plot_tree(dt_model, feature_names=df[['study', 'attendance', 'assignments']].columns, filled=True)
plt.show()
"""
