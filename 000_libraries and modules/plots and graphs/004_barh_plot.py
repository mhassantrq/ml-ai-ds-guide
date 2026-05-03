import matplotlib.pyplot as plt
import random

x = [1, 2, 3, 4, 5]
y = [random.randint(0,100) for _ in range(5)]

plt.barh(x, y)
plt.show()