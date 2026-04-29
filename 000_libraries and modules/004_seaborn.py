import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/data.csv')

#   1. to draw line plot
#sns.lineplot(x='area', y='amount', data=df)

#   2. to draw bar plot
#sns.barplot(x='area', y='amount', data=df)

#   3. to draw histogram
#sns.histplot(data=df['amount'])

#   4. to draw pair plot
#sns.pairplot(data=df)

#   5. to draw violin plot
#sns.violinplot(x='area', y='amount', data=df)


plt.show()