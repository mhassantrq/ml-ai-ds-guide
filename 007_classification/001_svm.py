"""
SVM using sklearn
SVM can be used for both classification and regression.
"""

import pandas as pd
from sklearn.svm import SVC


df = pd.read_csv('data/classification01.csv')

svc_model = SVC()
svc_model.fit(df[['study']], df.result)

pred_result = svc_model.predict([[3]])
print(pred_result)