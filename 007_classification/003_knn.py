import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


df = pd.read_csv('data/classification01.csv')

knn_model = KNeighborsClassifier()

knn_model.fit(df[['study']], df.result)
pred_result = knn_model.predict([[10]])

print(pred_result)