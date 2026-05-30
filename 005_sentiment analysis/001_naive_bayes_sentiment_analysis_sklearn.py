"""
this is the implementation of naive bayes from sklearn for purpose of sentiment analysis
"""
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('data/dataset01.csv')

#print(df.columns)   #   get column names

#print(df.groupby('tag').describe())   #   view the count of each type of sentiment tag, positive and negative

df['sentiment'] = df['tag'].apply(lambda tag: 0 if 'negative' in tag else 1)

#print(df.groupby('sentiment').describe())   #   check if numerical values are correctly inserted

train_X, test_X, train_y, test_y = train_test_split(df.text, df.sentiment, test_size=0.2)

vectorizer = CountVectorizer()

train_count_vectorizer = vectorizer.fit_transform(train_X)
#train_count_vectorizer = train_count_vectorizer.toarray()

test_count_vectorizer = vectorizer.transform(test_X)
#test_count_vectorizer = test_count_vectorizer.toarray()


#bayes_model = GaussianNB()

bayes_model = MultinomialNB()

bayes_model.fit(train_count_vectorizer, train_y)

score = bayes_model.score(test_count_vectorizer, test_y)

print(score)