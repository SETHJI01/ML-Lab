import numpy as np
import pandas as pd
from math import exp
from sklearn.model_selection import train_test_split
data= pd.read_csv('LogisticCsv.csv')
def normalize(X):
    return X-X.mean()

def predict(X,b0,b1):
    return np.array([1/(1+exp(-1*b0 + -1*b1*x)) for x in X])

def logisticRegression(X,Y):
    b0=0
    b1=0
    L=0.001
    epochs=300
    X=normalize(X)
    for i in range(epochs):
        y_pred=predict(X,b0,b1)
        d_b0=-2*sum((Y-y_pred)*y_pred*(1-y_pred))
        d_b1=-2*sum(X*(Y-y_pred)*y_pred*(1-y_pred))
        b0=b0-L*d_b0
        b1=b1-L*d_b1
    return b0,b1

X_train,X_test,Y_train,Y_test=train_test_split(data['Age'],data['Purchased'],test_size=0.3)
b0,b1=logisticRegression(X_train,Y_train)
X_test_Norm=normalize(X_test)
y_pred=predict(X_test_Norm,b0,b1)
for i in range(len(y_pred)):
    if(y_pred[i]>=0.5):
        y_pred[i]=1
    else:
        y_pred[i]=0


#checking accuracy
count=0
for i in range(len(y_pred)):
    if(y_pred[i]==Y_test.iloc[i]):
        count=count+1
print(f"accuracy =  {count/len(y_pred)}")