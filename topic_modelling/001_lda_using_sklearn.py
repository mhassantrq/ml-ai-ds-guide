import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

df = pd.read_csv('data/dataset.csv')

vect = CountVectorizer()
words_count = vect.fit_transform(df['text'][0:5])

words = vect.get_feature_names_out()

lda = LatentDirichletAllocation(n_components=2, random_state=43)
lda.fit(words_count)

t_list = []

for t in lda.components_:
    top = t.argmax()
    t_list.append(words[top])

print(t_list)