"""
Term frequency, inverse document frequency. It is used to determine how important a word is to a document.
"""

#   import tfidf vectorizer from sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

#   read data
df = pd.read_csv('data/dataset.csv')

#   just to view the dataset 
print(df['text'][0:5])

#   initialize the vectorizer object
vect = TfidfVectorizer()

#   to get vocabulary, idf value and convert text into number
tfidf_arr = vect.fit_transform(df['text'][0:5])

#   now get all unique words in the dataset
unique_words = vect.get_feature_names_out()

#   print the list of all unique words
print(f'Unique Words: {unique_words}')

#   the matrix to represent the tf-idf values
print(f'tf-idf Array: {tfidf_arr.toarray()}')

"""

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