import pandas as pd
import numpy as np 
df= pd.read_csv('points.csv')
k=3
threshold=2
epoch=1
size=len(df)
col_size = len(df.columns)
#without threshold
centroids=[]
for i in range(min(k,size)):
    arr=[]
    for j in range(len(df.iloc[i])):
        arr.append(df.iloc[i][j])
    centroids.append(arr)
import copy
import math
n=0
while n<epoch:
    n=n+1
    clusters=[]
    points=[]
    for i in range(len(centroids)):
        clusters.append([-1])
    for i in range(len(df)):
        arr=df.iloc[i].to_numpy()
        dist=[]
        for j in range(len(centroids)):
            x=0
            for l in range(len(arr)):
                x+=(int)((centroids[j][l]-arr[l])*(centroids[j][l]-arr[l]))
            x=math.sqrt(x)
            dist.append([x,j])
        for j in range(len(centroids)):
            arr1=df.iloc[points[j][0]].to_numpy()
            x=0
            for l in range(len(arr)):
                x+=(int)((arr1[l]-arr[l])*(arr1[l]-arr[l]))
            x=math.sqrt(x)
            dist.append([x,point[j][1]])
        dist.sort()
        cluster_size=len(clusters)
        clusters[dist[0][1]].append(i)
        points.append([i,dist[0][1]])
    prev_centroids=copy.deepcopy(centroids) 
    centroids.clear()
    points.clear()
    for i in clusters:
        del i[0]
    print("Epoch ",n,end="\n\n")
    print("\tCentroids : ",prev_centroids,end="\n\n")
    print("\tCluster : ",clusters,end="\n\n")

#with threshold=2

centroids=[]
for i in range(min(k,size)):
    arr=[]
    for j in range(len(df.iloc[i])):
        arr.append(df.iloc[i][j])
    centroids.append(arr)
import copy
import math
n=0
while n<epoch:
    n=n+1
    clusters=[]
    points=[]
    for i in range(len(centroids)):
        clusters.append([-1])
    for i in range(len(df)):
        arr=df.iloc[i].to_numpy()
        dist=[]
        for j in range(len(centroids)):
            x=0
            for l in range(len(arr)):
                x+=(int)((centroids[j][l]-arr[l])*(centroids[j][l]-arr[l]))
            x=math.sqrt(x)
            dist.append([x,j])
        for j in range(len(centroids)):
            arr1=df.iloc[points[j][0]].to_numpy()
            x=0
            for l in range(len(arr)):
                x+=(int)((arr1[l]-arr[l])*(arr1[l]-arr[l]))
            x=math.sqrt(x)
            dist.append([x,points[j][1]])
        dist.sort()
        cluster_size=len(clusters)
        if dist[0][0]<=threshold:
            clusters[dist[0][1]].append(i)
            points.append([i,dist[0][1]])
        else:
            clusters.append([-1,i])
            points.append([i,cluster_size])
    prev_centroids=copy.deepcopy(centroids) 
    centroids.clear()
    points.clear()
    for i in clusters:
        del i[0]
    print("Epoch ",n,end="\n\n")
    print("\tCentroids : ",prev_centroids,end="\n\n")
    print("\tCluster : ",clusters,end="\n\n")
