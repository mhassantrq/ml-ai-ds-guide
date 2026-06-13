"""
Principal Component Analysis
"""

import pandas as pd
from sklearn.decomposition import PCA


df = pd.read_csv('data/classification01.csv')
pca = PCA(n_components=2)

X = pca.fit_transform(df[['study', 'attendance', 'assignments', 'mid', 'final']])

print(X)