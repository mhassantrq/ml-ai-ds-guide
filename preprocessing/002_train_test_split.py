"""
Datasets almost always need to be split among training and testing data.
Training data is used to train the model while testing data is used to view how much accuracy 
has been achieved by the trained model.
"""

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/data.csv')

X = df[['city', 'age']]
y = df['salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

print(f'records of training set {len(X_train)}')
print(f'records of test set {len(X_test)}')