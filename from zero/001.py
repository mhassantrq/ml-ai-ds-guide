import pandas as pd

df = pd.read_csv('data/dataset.csv')

text_list = list(df['text'])

original_text = ''
for r in text_list:
    original_text += r

print(f'First 1000 characters in original text \n {original_text[:1000]}')
