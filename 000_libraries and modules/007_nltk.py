"""
Natural Language Toolkit - nltk
"""

import nltk
import pandas as pd

df = pd.read_csv('data/dataset01.csv')
text = df['text'][0]


"""
tokenization using nltk has two options, 
tokenize words or tokenize sentences.
for more on the topic tokenization itself, refer to tokenization file in preprocessing folder.
"""

word_tokens = nltk.word_tokenize(text)
sent_tokens = nltk.sent_tokenize(text)

print(f'word tokens: {word_tokens}')
print(f'sentence tokens: {sent_tokens}')
