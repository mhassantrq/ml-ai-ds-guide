"""
Term frequency, inverse document frequency. It is used to determine how important a word is to a document.

each document is now a row in this matrix. and all the unique words are columns in the matrix.
in each row, the numbers are represented from 0 to maximum 1.
0 means word now present in respective document. and higher number means more relevant in the document.
for example, view the below matrix.

    w1      w2      w3      w4      w5
r1  0       0       0.5     0.4     0.6
r2  0.1     0       0       0.3     0.7
r3  0.2     0.3     0       0.4     0.5

in the above matrix,
the rows r1, r2 and r3 represent three distinct documents.
the columns w1, w2,and so on, represent the unique words in all the documents combined.

so, if in the row2 the word 4 represents a score of 0.4, this means that specific word is important in the document 2.
"""


"""
1. term frquency - onverse document frequency using sklearn
"""
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


df = pd.read_csv('data/dataset01.csv')

#print(df['text'][0:5])


vect = TfidfVectorizer()
tfidf_arr = vect.fit_transform(df['text'][0:5])

unique_words = vect.get_feature_names_out()

#print(f'Unique Words: {unique_words}')
#print(f'tf-idf Array: {tfidf_arr.toarray()}')


"""
2. term frequency - inverse document frequency from scratch without using sklearn
"""

from collections import Counter, defaultdict
import math

inversedf = defaultdict(int)
doc_word_count = defaultdict(int)

df_list = list(df['text'][0:5])
df_list = [row.lower().split() for row in df_list]

df_list = [Counter(row) for row in df_list]

words = ' '.join(df['text'][0:5].astype(str).values.flatten()).split()

for word in words:
    for i in range(len(df['text'][0:5])):
        if word in df['text'][i]:
            doc_word_count[word] += 1

for word in words:
    inversedf[word] = math.log(len(df_list) / doc_word_count[word])

for i in range(len(df_list)):
    for t in df_list[i]:
        termf = df_list[i][t] / len(df_list[i])
        termf_inversedf = termf*inversedf[t]
        print(f'For document {i} and term {t}, the termf-inversedf: {termf_inversedf}')