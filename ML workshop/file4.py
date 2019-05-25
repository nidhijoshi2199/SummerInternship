import numpy as nm
import matplotlib.pyplot as plt
import pandas as pd

dataset= pd.read_csv('Mall_Customers.csv')
features=dataset.iloc[:,[2,4]].values

#scatter all these data points on maplotlib
plt.scatter(features[:,0],features[:,1])
plt.show()

#using the elbow method to find the optimal no of clusters
from sklearn.cluster import KMeans


#fitting K means to dataset
kmeans =KMeans(n_clusters=3, init ='k-means++', random_state=0)
pred_cluster= kmeans.fit_predict(features)

#visualising the clusters
#plt.scatter
plt.scatter(features[pred_cluster==0,0], features[pred_cluster==0,1], c='red', label='cluster1')
plt.scatter(features[pred_cluster==1,0], features[pred_cluster==1,1], c='green', label='cluster2')
plt.scatter(features[pred_cluster==2,0], features[pred_cluster==2,1], c='blue', label='cluster3')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], c='yellow', label='centroid')

plt.title('cluter of customers')
plt.xlabel('annual income(k$)')
plt.ylabel('Spending score(1-100)')
plt.legend()
plt.show()