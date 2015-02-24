
# coding: utf-8

# In[4]:

import numpy as np
import pandas as pd
import sklearn
from sklearn.cluster import KMeans
from sklearn import metrics


# In[5]:

df = pd.read_csv("yelp_reviewers.txt", delimiter="|")
print df.head()


# ### Q2

# In[8]:

def fit_k_means(k_values, X, calc_ss):
    models = {}
    for k in k_values:
        k_means = sklearn.cluster.KMeans(n_clusters=k)
        k_means.fit(X)
        models[k] = k_means
        if calc_ss:
            print "K: %s -> SS: %s" % (k, calc_silhouette_score(X, k_means.labels_, 1000))
    return models
    
def calc_silhouette_score(X, labels, sample_size):
    # only use 10k points for score due to resource constraints
    return sklearn.metrics.silhouette_score(X
                                            , labels
                                            , metric='euclidean'
                                            , sample_size=sample_size)


# In[9]:

k_values = range(2,9)
# print df[["q4", "q5", "q6"]].head()
q2_features = df[[2,3,4]].values
# print q2_features.shape, type(q2_features)

fit_k_means(k_values, q2_features, 1)


# ## Q3

# In[10]:

q3_features = df[["q8", "q9", "q10"]].dropna().values
fit_k_means(k_values, q3_features, 1)


# ## Q4

# In[11]:

q4_features = df[["q11", "q12", "q13"]].dropna().values
fit_k_means(k_values, q4_features, 1)


# ## Q5

# In[12]:

# List the number of data points in each cluster
q4_features = df[["q11", "q12", "q13"]].dropna().values
q4_model = fit_k_means([8], q4_features, 1)


# In[23]:

k_8_modelq4 = q4_model.get(8)
labels = k_8_modelq4.labels_
centroids = k_8_modelq4.cluster_centers_

count_by_centroid = {}
for i in range(0,len(centroids)):
    count_by_centroid[i] = 0
    
for c in labels:
    count_by_centroid[c] += 1

print count_by_centroid


# In[22]:




# In[ ]:



