"""
Another method to vectorize text data. This pretty straight forward and basic method.
It is just the total count of every single word in a given input text data.
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from collections import defaultdict

"""
Reading dataset, but only storing first 1000 rows in the text variable for preprocessing purpose.
"""
df = pd.read_csv('data/dataset01.csv')
text = df['text'][0:1000]

#   1.  Using CountVectorizer

vectr = CountVectorizer()
word_vectors = vectr.fit_transform(text)

print('1. Using CountVectoizer')
print(vectr.get_feature_names_out())

print(word_vectors.toarray())

"""
in above lines.
get_feature_names_only() function will return the names of features. in this cases, every single word.
then in next line, the toarray() function will convert the word vectors into array, so that we are
easily able to see the vectors we have created for out text.
"""


#   2.  Manually using defaultdict

#   creating a list of words
text = text[0].split()

bagofwords = defaultdict(int)

for w in text:
    bagofwords[w] += 1

"""
the above loop will iterate over every word in the text.
each words will have its own index position in bagofwords defaultdict represented by the word itself.
And every occurance of the word will be counted in loop.
"""

print(bagofwords)