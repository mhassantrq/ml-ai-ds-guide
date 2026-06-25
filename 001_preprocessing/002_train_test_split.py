"""
Datasets almost always need to be split among training and testing data.
Training data is used to train the model while testing data is used to view how much accuracy 
has been achieved by the trained model.
"""

# import pandas to read cav file in data frame
import pandas as pd

# import train_test_split from sklearn to split the data
from sklearn.model_selection import train_test_split

# read file
df = pd.read_csv('data/data.csv')

# x values include city and age from data frame
X = df[['city', 'age']]

# y variable salary, to be predicted based on coty and age
y = df['salary']

# split
# test size=0.3 means that data to be split 70 and 30 percent for train and test respectively
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

print(f'records of training set {len(X_train)}')
print(f'records of test set {len(X_test)}')


"""
However, train test split can be done manually by simple dividing the dataset into separate containers of train and test labels.

for example:

if a dictionary named 'data' has dataset of say 1000 rows. and you want to separate it into 80-20 split manually.
then you may proceed as follows:

train_size = len(data)*0.8
train_size = int(train_size)

train_data = data[:train_size]
test_data = data[train_size:]

this way using slicing, the 'train_data' container will have data from 0 up until train_size which in our example is 799.
and 'test_data' will contain data from 800 to 1000.
"""