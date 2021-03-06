#!/usr/bin/env python
# coding: utf-8

# In[2]:


# KNN Classification
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier


# In[4]:


glass=pd.read_csv('C:/Users/prate/Downloads/Assignment/KNN/glass.csv',error_bad_lines=False)

glass.head()


# In[5]:


X=glass.iloc[:,0:9]
Y=glass.iloc[:,9:]


# In[6]:


num_folds = 10
kfold = KFold(n_splits=10)


# In[7]:


model = KNeighborsClassifier(n_neighbors=17)
results = cross_val_score(model, X, Y, cv=kfold)


# In[8]:


print(results.mean())


# ### Grid Search for Algorithm Tuning

# In[9]:


# Grid Search for Algorithm Tuning
import numpy
from pandas import read_csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV


# In[10]:


n_neighbors = numpy.array(range(1,40))
param_grid = dict(n_neighbors=n_neighbors)


# In[11]:


model = KNeighborsClassifier()
grid = GridSearchCV(estimator=model, param_grid=param_grid)
grid.fit(X, Y)


# In[12]:


print(grid.best_score_)
print(grid.best_params_)


# ### Visualizing the CV results

# In[13]:


import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
# choose k between 1 to 41
k_range = range(1, 41)
k_scores = []
# use iteration to caclulator different k in models, then return the average accuracy based on the cross validation
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, Y, cv=5)
    k_scores.append(scores.mean())
# plot to see clearly
plt.plot(k_range, k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.show()


# In[ ]:




