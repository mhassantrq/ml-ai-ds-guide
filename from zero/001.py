import pandas as pd
import re

df = pd.read_csv('data/dataset.csv')

text_list = list(df['text'])

original_text = ''
for r in text_list:
    original_text += r

print(f'First 1000 characters in original text \n {original_text[:1000]}')

#   lets see how many characters does it have
print(len(original_text))   #   outputs 65 million plus.

#   we ll only use 10000 characters for further understanding
updated_text = original_text[:10000]
print(len(updated_text))


#   lets tokenize them
tokens = updated_text.split(' ')
print(tokens[:10])

"""
this above given straight forward method of tokenization is not useful as white spaces are removed and we cannot use tokens' sequence

lets use regular expressions for this purpose
"""

