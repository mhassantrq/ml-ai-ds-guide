"""
Linear Regression using scipy
"""

# import stats from scipy package
from scipy import stats
# import matplotlib to plot graph of data
import matplotlib.pyplot as plt
import random

# generating random values for x and y labels
x_values = [random.randint(10, 90) for _ in range(15)]
y_values = [random.randint(80, 250) for _ in range(15)]

# put values of x and y on graph
plt.scatter(x_values, y_values)
#   plt.show()

m, y, r, p, err = stats.linregress(x_values, y_values)

#   m:      slope. it shows the change in x and y relation. positive means upward trend, while negative shows downward trend.
#   y:      y-intercept.
#   r:      correlation coefficient. values between 1 and -1. near to 1 or -1 means strong relationship.
#   p:      p-value. if less than 0.05. it means relation is significant. above 0.05, then due to randomness.
#   err:    standard error.

lin_model = [m * var + y for var in x_values]

plt.plot(x_values, lin_model)

#plt.show()

print(r)