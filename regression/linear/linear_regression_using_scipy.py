"""
Linear Regression using scipy
"""

from scipy import stats
import matplotlib.pyplot as plt
import random

x_values = [random.randint(10, 90) for _ in range(15)]
y_values = [random.randint(80, 250) for _ in range(15)]

plt.scatter(x_values, y_values)
#   plt.show()

m, y, r, p, err = stats.linregress(x_values, y_values)

lin_model = [m * var + y for var in x_values]

plt.plot(x_values, lin_model)

plt.show()