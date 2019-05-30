import numpy as np
import pandas as pd

#importing dataset
dataset= pd.read_csv('Salaries.csv')
features=dataset.iloc[:,2:3].values
labels=dataset.iloc[:,-1].values

#splitting the datasets into the training set and test set
from sklearn.model_selection import train_test_split 
features_train,features_test,label_train, label_test=train_test_split(features, labels, test_size=0.2, random_state=0)


#fitting simple linear regression to the training set
from sklearn.linear_model import LinearRegression

regressor=LinearRegression()
regressor.fit(features_train,label_train)
value = np.array([40]).reshape(1, -1)
regressor.predict(value)