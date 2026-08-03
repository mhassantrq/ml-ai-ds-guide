"""
Natural Language Toolkit - nltk
"""

import nltk
import pandas as pd

df = pd.read_csv('data/dataset01.csv')
text = df['text'][0]


"""
1. tokenization
tokenization using nltk has three options, 
tokenize words, tokenize sentences or tokenize using regular expressions.

for more on the topic tokenization itself, refer to tokenization file in preprocessing folder.
for more no learning regular expressions, refer to regular expressions file in preprocessing folder.
"""

word_tokens = nltk.word_tokenize(text)
sent_tokens = nltk.sent_tokenize(text)
regex_tokens = nltk.regexp_tokenize(text, pattern='\w+')

print(f'word tokens: {word_tokens}')
print(f'sentence tokens: {sent_tokens}')
print(f'regular expression tokens: {regex_tokens}')


"""
2. 
"""