"""
Somewhat similar to the previous bag of words.
However, a key difference. The ngrams consider words not word (singular) for their counts.
It assumes that words appearing together have more significance.
It can be unigram, bigram, trigram or more. 
in below example, we try the bigram i.e., two words.
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('data/dataset01.csv')
text = df['text'][100:150]

"""
in object creation, we pass the ngram value below using the ngram_range
the first parameter to this is the minimum word limit and second parameter is the maximum word limit.
"""
vectr = CountVectorizer(ngram_range=(2,2))

word_vectors = vectr.fit_transform(text)

print(vectr.get_feature_names_out())

