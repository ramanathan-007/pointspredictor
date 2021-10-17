import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd

dataset =pd.read_csv('data.csv')

dataset['goals%'].fillna(dataset['goals%'].mean(), inplace=True)

X=dataset.iloc[:, :3]

y= dataset.iloc[:, -1]

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(X,y)

pickle.dump(regressor, open('main.pkl','wb'))

main = pickle.load(open('main.pkl','rb'))
print(main.predict([[6.8, 0.5,0.6]]))


