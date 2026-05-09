import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('data/dataset01.csv')
text = df['text'][100:150]

vectr = CountVectorizer(ngram_range=(2,2))

word_vectors = vectr.fit_transform(text)

print(vectr.get_feature_names_out())