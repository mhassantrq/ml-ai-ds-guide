import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt


df = pd.read_csv('data/clustering01.csv')


agglomerative_model = AgglomerativeClustering(n_clusters=2)

clusters_predict = agglomerative_model.fit_predict(df[['name', 'exp']])

df['cluster'] = clusters_predict

cluster_0 = df[df['cluster'] == 0]
cluster_1 = df[df['cluster'] == 1]

plt.scatter(cluster_0['name'], cluster_0['exp'])
plt.scatter(cluster_1['name'], cluster_1['exp'])

plt.show()