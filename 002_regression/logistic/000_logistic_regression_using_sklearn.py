"""
Logistic Regression
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


df = pd.read_csv('data/classification01.csv')

model = LogisticRegression()
model.fit(df[['study']], df.result)

pred_result = model.predict([[10]])

print(pred_result)

plt.scatter(df.study, df.result)
plt.scatter(10, pred_result)
plt.show()
