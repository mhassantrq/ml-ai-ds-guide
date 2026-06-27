"""
Principal Component Analysis

this is a dimensionality reduction technique. used to reduce the number of features, as a result, reducing the time for model training and testing.

"""

import pandas as pd
from sklearn.decomposition import PCA


df = pd.read_csv('data/classification01.csv')

pca = PCA(n_components=2)   #   value passed as parameter is the intended number of features to retain

X = pca.fit_transform(df[['study', 'attendance', 'assignments', 'mid', 'final']])

print(X)