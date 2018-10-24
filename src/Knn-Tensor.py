#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:52:28 2018

@author: amajidsinar
"""

from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-white')

iris = datasets.load_iris()

dataset = iris.data
# only take 0th and 1th column for X
data_known = iris.data[:,:2]
# y
label_known = iris.target

# the hard part
# so matplotlib does not readily support labeling based on class
# but we know that one of the feature of plt is that a plt call would give those set of number
# the same color
category = np.unique(label_known)
for i in category:
    plt.scatter(data_known[label_known==i][:,0],data_known[label_known==i][:,1],label=i)

# Unknown class of a data
data_unknown = np.array([[5.7,3.3],[5.6,3.4],[6.4,3],[8.2,2.2]])
plt.scatter(data_unknown[:,0],data_unknown[:,1], label='?')
plt.legend()
#-------------
# Euclidean Distance
diff = data_known - data_unknown.reshape(data_unknown.shape[0],1,data_unknown.shape[1])
distance = (diff**2).sum(2)

#return sorted index of distance
dist_index = np.argsort(distance)
label = label_known[dist_index]

#for k in [1,2,3,4,5,6,7,8,9,10]:
#keep the rank
k = 10
label = label[:,:k]

label_predict = []
for i in range(data_unknown.shape[0]):
    values,counts =  np.unique(label[i], return_counts=True)
    ind = np.argmax(counts)
    label_predict.append(values[ind])
    
    






    
    




