"""
ANN
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch, torch.nn as nn

df = pd.read_csv('data/classification01.csv')

print(f'At Start: \n{df}')

df['result'] = df['result'].map({'F':0, 'P':1})

print(f'After Result Map: \n{df}')

X = df[['study', 'attendance', 'assignments']].values
y = df['result'].values

print(f'X values: {X}')
print(f'y values: {y}')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)

y_train = torch.tensor(y_train, dtype=torch.float32).view(-1,1)
y_test = torch.tensor(y_test, dtype=torch.float32).view(-1,1)

print(X_train.shape)
print(y_train.shape)

nn_model = nn.Sequential(nn.Linear(3,1), nn.Sigmoid())

nn_loss = nn.BCELoss()
nn_optmzr = torch.optim.SGD(nn_model.parameters(), lr=0.01)

for epoch in range(15):
    y_pred = nn_model(X_train)
    loss = nn_loss(y_pred,y_train)

    nn_optmzr.zero_grad()
    loss.backward()
    nn_optmzr.step()

    print(loss.item())

with torch.no_grad():
    test_pred = nn_model(X_test)
    predtd = (test_pred >= 0.5).float()

    acc = (predtd == y_test).float().mean()

    print(f'Accuracy: {acc.item()}')
