import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def calculate(x1,x2):
    return np.sqrt(np.sum(np.square(x1-x2)))

def predict(X_train,Y_train,X_test,k):
    distances=[]
    for i in range(len(X_train)):
        dist=calculate(X_train[i],X_test)
        distances.append(tuple([dist,Y_train[i]]))
    closeset_k=sorted(distances)[:k]
    print(closeset_k)
    ans=[]
    for i in range(len(closeset_k)):
        ans.append(closeset_k[i][1]) 
    res=ans[0]
    counter=0
    for i in range(len(ans)):
        current_count=ans.count(ans[i])
        if(current_count>counter):
            counter=current_count
            res=ans[i]
    return res



data=pd.read_csv("Climate_Data.csv")
X=np.array(data)[:,1:-1]
Y=np.array(data)[:,-1]
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=0)
for i in range(len(X_test)):
    y_pred=predict(X_train,Y_train,X_test[i],5)
