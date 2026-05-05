import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from collections import defaultdict
import re

df = pd.read_csv('data/dataset.csv')

temp_dataset = df['text'][0:5]
dataset = []

for d in temp_dataset:
    d = re.sub(r'<.*?>', '', d)
    d = d.lower()
    dataset.append(d)

#vect = CountVectorizer(stop_words='english')
vect = TfidfVectorizer(stop_words='english')
words_count = vect.fit_transform(dataset)

words = vect.get_feature_names_out()

lda = LatentDirichletAllocation(n_components=5)
lda.fit(words_count)

t_list = []

for t in lda.components_:
    top = t.argmax()
    t_list.append(words[top])

print(t_list)