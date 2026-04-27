from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np

x_data = [5,6,2,10,15,20,7,8]
y_data = [50,55,25,110,150,180,80,90]

plt.scatter(x_data,y_data)

plt.xlabel = 'Area'
plt.xlabel = 'Price'

x_data = np.array(x_data).reshape(-1,1)

lin_model = linear_model.LinearRegression()
lin_model.fit(x_data, y_data)

print(lin_model.predict([[50]]))

plt.plot(x_data, lin_model.predict(x_data), color='red')

plt.show()