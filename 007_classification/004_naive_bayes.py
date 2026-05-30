"""
Naives bayes using sklearn
"""

import pandas as pd
from sklearn.naive_bayes import MultinomialNB, GaussianNB


df = pd.read_csv('data/classification01.csv')

#   1. Multinomial Naive Bayes

mn_model = MultinomialNB()
mn_model.fit(df[['study', 'attendance', 'assignments']], df.result)

print(mn_model.predict([[12, 95, 3]]))


#   2. Gaussian Naive Bayes

g_model = GaussianNB()
g_model.fit(df[['study', 'attendance', 'assignments']], df.result)

print(g_model.predict([[12, 95, 3]]))