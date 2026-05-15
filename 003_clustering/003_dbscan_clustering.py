import pandas as pd
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt


df = pd.read_csv('data/clustering01.csv')


dbscan_model = DBSCAN(eps=3, min_samples=2)

dbscan_model.fit(df[['name', 'exp']])

print(dbscan_model.labels_)

plt.scatter(df['name'], df['exp'], c=dbscan_model.labels_)

plt.show()