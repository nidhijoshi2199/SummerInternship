import pandas as pd
import numpy as nm

#importing dataset
dataset= pd.read_csv('Salaries.csv')
features=dataset.iloc[:,[0,2,3]].values
labels=dataset.iloc[:,-1].values

#taking care of missing data
from sklearn.preprocessing import Imputer
imputer =Imputer(
        missing_values='NaN',
        strategy='mean', axis=0)
imputer=imputer.fit(features[:,1:2])
features[:,1:2]=imputer.transform(features[:,1:2])

#missing value handling in labels
label=labels.reshape(-1,1)
imputer=imputer.fit(labels)
labels=imputer.transform

#encoding categorical data

#encoding the indepedent variable
from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
features[:,0]=labelencoder.fit_transform(features[:,0])


#onehotencoding the labelled data
'''from sklear.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[0])
'''

