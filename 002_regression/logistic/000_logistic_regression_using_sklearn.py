"""
Logistic Regression using sklearn

Logistic regression is used to predict class in binary classification cases.
It uses sigmoid function to convert values between 0 and 1 for finding out probabilities.

Logistic regression is a supervised algorithm. Therefore, it requires labelled dataset.

Below is the implementation of logistic regression using sklearn.
However, if you're interested in its implementation from scratch. The same is available in the
repo named: 'trying-ml-models-from-scratch'
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
