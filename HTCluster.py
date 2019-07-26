# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 17:22:52 2016

@author: marckendal
"""

from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq
from sklearn import datasets
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np

HTData = pd.read_csv('Final_Decisions_2015_Total_Removed.csv')
#print (HTData.head()) # check if everything is in place
HTData_Columns = len(HTData.columns)
print(HTData_Columns)
data = HTData.as_matrix()
#
## get the known cluster labels into a separate array
## in practical cases, you might not already have such information
## but when you do, these might be used to either evaluate or "supervise"
## the model you are trying to build
classLabelsKnown = np.asarray(data[:,0]) 
##classLabelsKnown -= 1 # get the labels start from 0
#
##DataToCluster = HTData.as_matrix(['Referals in 2015','Positive Reasonable Grounds Decision'])
HTData_Minus_Countries = HTData.iloc[:,1:12]
DataToCluster = HTData_Minus_Countries.as_matrix()
#
print(DataToCluster)
# get all the data but not the class labels
#DataToCluster = data[:,1::]

#computing K-Means with K = 3 (3 clusters)
kmeansModel = KMeans(init='random', n_clusters=3, n_init=10)
kmeansModel.fit_predict(DataToCluster)
clusterResults = kmeansModel.labels_


#d = []
#for i, clustLabel in enumerate(clusterResults):
#    d.append({'Cluster result': clustLabel, 'Known labels': classLabelsKnown[i], })
#
#df_KMeans_Cluster = pd.DataFrame(d)
#df_KMeans_Cluster.to_csv('Cluster_Results.csv')
## Let's check the results and try to compare with known labels
for i, clustLabel in enumerate(clusterResults):
 print("Cluster result: ", clustLabel, " Known labels: ",classLabelsKnown[i])
 
 



