import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


df = pd.read_csv('data/clustering01.csv')

#   print(df)

kmeans_model = KMeans(n_clusters=2)
