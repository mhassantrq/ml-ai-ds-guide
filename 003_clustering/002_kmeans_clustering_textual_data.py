import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv('data/dataset01.csv')

# print(df.columns)
# print(df.shape)
"""
Since we are not dealing with numbers but text. We first need to convert the text into numbers
CountVectorizer with count every word the number of times its appearing.
More explanation of CountVectorizer is in the Preprocessing directory in files of bagofwords and ngrams.
"""
vectorizer = CountVectorizer(stop_words='english', max_features=1000)
text_vectors = vectorizer.fit_transform(df['text'])

"""
The first step is to create an object of the kmeans clustering model.
We pass cluster value 2 in this case.
Any value can be passed depending upon the number of clusters needed.
"""
kmeans_model = KMeans(n_clusters=2)

df['tag'] = kmeans_model.fit_predict(text_vectors)

plt.pie(df['tag'].value_counts())
plt.show()