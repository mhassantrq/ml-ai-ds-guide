import matplotlib.pyplot as plt
import random

x = [random.randint(0,20) for _ in range(10)]
y = [random.randint(0,100) for _ in range(10)]

plt.scatter(x, y)
plt.show()