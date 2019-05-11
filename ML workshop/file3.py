import numpy as np
import pandas as pd

#we import this dataset already in sklearn and perform 
from sklearn.datasets import load_iris

iris=load_iris()
print (iris.feature_names) #cloumn names for iris data

#splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train,labels_test =train_test_split(
        iris.data, iris.target,test_size=0.25,
        random_state=0)

#fitting logistic regression to training set
from sklearn.linear_model import LogisticRegression
logClassifier=LogisticRegression(random_state=0)
logClassifier.fit(features_train, labels_train)

#print score for the regression model
print (logClassifier.score(features_train, labels_train))

#predicting the Test set results
val=features_test[17].reshape(1,-1)
labels_pred= logClassifier.predict(features_test)
single_pred= logClassifier.predict(features_test[17,:].reshape(1,-1)[0])
print (iris.target_names[single_pred])


#making the confusion matrix
from sklearn.metrics import confusion_matrix
cm= confusion_matrix(labels_test, labels_pred)
