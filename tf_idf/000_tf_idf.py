"""
Term frequency, inverse document frequency. It is used to determine how important
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

df = pd.read_csv('data/dataset.csv')

print(df['text'][0:5])

vect = TfidfVectorizer()
tfidf_arr = vect.fit_transform(df['text'][0:5])

unique_words = vect.get_feature_names_out()

print(f'Unique Words: {unique_words}')

print(f'tf-idf Array: {tfidf_arr.toarray()}')