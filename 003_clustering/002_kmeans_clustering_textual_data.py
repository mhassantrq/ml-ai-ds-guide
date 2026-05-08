import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv('data/dataset01.csv')

# print(df.columns)
# print(df.shape)

vectorizer = CountVectorizer(stop_words='english', max_features=1000)
text_vectors = vectorizer.fit_transform(df['text'])

kmeans_model = KMeans(n_clusters=2)

df['tag'] = kmeans_model.fit_predict(text_vectors)

plt.pie(df['tag'].value_counts())
plt.show()