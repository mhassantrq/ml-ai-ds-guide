import pandas as pd
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('data/dataset01.csv')

text = df['text'][0:10]

print(text[0])
print('================')

#   1.  Using handmade list of stop words

stopwords = pd.read_csv('data/stopwords.csv')
stopwords = list(stopwords['words'])

updated_text = []

for w in text[0].split():
    if w.lower() not in stopwords:
        updated_text.append(w)

#print(updated_text)


#   2. Using stop words from sklearn

updated_text = []

for w in text[0].split():
    if w.lower() not in ENGLISH_STOP_WORDS:
        updated_text.append(w)

#print(updated_text)


#   3. Using stop words from CountVectorizer

vctr = CountVectorizer(stop_words='english')

word_vectors = vctr.fit_transform(text)

print(vctr.get_feature_names_out())