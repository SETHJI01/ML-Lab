import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
data=pd.read_csv("clustering.csv")
data=data.loc[:,['ApplicantIncome', 'LoanAmount']]
X=data.values
def kmeans(X,k):
    max_iterations=100
    clusters=np.zeros(len(X))
    rndIdx=np.random.choice(len(X),size=k,replace=False)
    centroids=X[rndIdx,:]
    check=1
    while check:
        max_iterations=max_iterations-1
        for i, x in enumerate(X):
            mini=float('inf')
            for j, centroid in enumerate(centroids):
                d=np.sqrt(np.sum(np.square(centroid-x)))
                if(mini>d):
                    mini=d
                    clusters[i]=j
        modified_centroids=pd.DataFrame(X).groupby(by=clusters).mean().values
        if max_iterations==0:
            break
        if np.array_equal(centroids,modified_centroids):
            check=0
        else:
            centroids=modified_centroids
    return centroids,clusters
        
k = 3
centroids, cluster = kmeans(X, k)
    
