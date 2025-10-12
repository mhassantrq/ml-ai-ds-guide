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
this above given straight forward method of tokenization is not useful enough

lets use regular expressions for this purpose to include empty spaces as well as some puntuations for split
"""

tokens = re.split(r'(\s|[.,:;])', updated_text)
print(tokens[:100])      #   tokens inclusing empty spaces

updated_tokens = [t for t in tokens if t and not t.isspace()]
print(updated_tokens[:100])