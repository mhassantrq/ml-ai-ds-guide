import matplotlib.pyplot as plt
import random

x = ['Maths', 'Physics', 'Chemistry', 'Biology', 'CS']
y = [random.randint(1, 100) for _ in range(5)]

plt.pie(y, labels=x)
plt.show()