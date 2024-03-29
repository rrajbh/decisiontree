#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:21:56 2019

@author: rajat.rajbhandari
"""

import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns; sns.set()



from sklearn.datasets import make_blobs
X, y = make_blobs(n_samples=300, centers=4,random_state=0, cluster_std=1.0)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='rainbow')

from sklearn.tree import DecisionTreeClassifier 
tree = DecisionTreeClassifier().fit(X, y)



def visualize_classifier(model, X, y, ax=None, cmap='rainbow'): 
   ax = ax or plt.gca()
    # Plot the training points
   ax.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=cmap,
              clim=(y.min(), y.max()), zorder=3)
   ax.axis('tight')
   ax.axis('off')
   xlim = ax.get_xlim()
   ylim = ax.get_ylim()
   # fit the estimator
   model.fit(X, y)
   xx, yy = np.meshgrid(np.linspace(*xlim, num=200),np.linspace(*ylim, num=200))
   Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
   
   # Create a color plot with the results
   n_classes = len(np.unique(y))
   contours = ax.contourf(xx, yy, Z, alpha=0.3,
                          levels=np.arange(n_classes + 1) - 0.5,
                          cmap=cmap, clim=(y.min(), y.max()),
                          zorder=1)
   ax.set(xlim=xlim, ylim=ylim)

visualize_classifier(DecisionTreeClassifier(),X,y)


