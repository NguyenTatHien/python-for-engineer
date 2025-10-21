import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('./Ecommerce Customers.csv')
# head = df.head()
# print('Head: \n', head)

# describe = df.describe()
# print('Describe: \n', describe)

# print('Info: ')
# info = df.info()
# print('Info: \n', info)

# sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=df)
# sns.jointplot(x='Time on App', y='Yearly Amount Spent', data=df)

# sns.jointplot(x='Time on App', y='Length of Membership', kind='hex', data=df)

# sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data=df)

X = customers[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = customers['Yearly Amount Spent']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=105)

lr_model = LinearRegression()

lr_model.fit(X_train, y_train)

plt.show()