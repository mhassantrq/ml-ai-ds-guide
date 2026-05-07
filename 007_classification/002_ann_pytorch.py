"""
ANN
"""

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/classification01.csv')

print(f'At Start: \n{df}')

df['result'] = df['result'].map({'F':0, 'P':1})

print(f'After Result Map: \n{df}')
