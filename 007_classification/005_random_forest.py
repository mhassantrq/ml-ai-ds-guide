"""
Random Forest using sklearn
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv('data/classification01.csv')

rf_model = RandomForestClassifier()
rf_model.fit(df[['study', 'attendance', 'assignments']], df.result)

print(rf_model.predict([[3,85,3]]))