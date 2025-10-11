import matplotlib.pyplot as plt
import random

x = [random.randint(1, 100) for _ in range(50)]

plt.hist(x, bins=20)
plt.show()