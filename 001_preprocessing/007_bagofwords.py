"""
Another method to vectorize text data. This pretty straight forward and basic method.
It is just the total count of every single word in a given input text data.
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from collections import defaultdict

df = pd.read_csv('data/dataset01.csv')
text = df['text'][0:1000]

#   1.  Using CountVectorizer

vectr = CountVectorizer()
word_vectors = vectr.fit_transform(text)

print('1. Using CountVectoizer')
print(vectr.get_feature_names_out())

print(word_vectors.toarray())

#   2.  Manually using defaultdict

text = text[0].split()
bagofwords = defaultdict(int)

for w in text:
    bagofwords[w] += 1

print(bagofwords)