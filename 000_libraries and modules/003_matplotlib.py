"""
perhaps the most popular library for visualization. 
many graphs, including bar chart, line graph, scatter plot etc.
"""

import matplotlib.pyplot as plt
import random

x_data = [random.randint(10,20) for _ in range(20)]
y_data = [random.randint(15,200) for _ in range(20)]

#   to draw scatter plot
#plt.scatter(x_data, y_data)

#   to draw line plot
#plt.plot(x_data, y_data)

#   to draw bar chart
#plt.bar(x_data, y_data)

#   to draw pie chart
#plt.pie(x_data, labels=y_data)

#   to draw box plot
#plt.boxplot(x_data)

plt.xlabel = 'x-axis'
plt.ylabel = 'y-axis'

plt.show()