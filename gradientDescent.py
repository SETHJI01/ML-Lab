import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def gradient_descent(x1,x2,x3,x4,y):
    m1=m2=m3=m4=b=0
    iterations = 1000
    n = len(x)
    alpha = 0.01

    for i in range(iterations):
        y_pred = m1*x1 + m2*x2 + m3*x3 + m4*x4 + b
        cost = (1/n)*sum([val**2 for val in (y-y_pred)])
        md1= -(2/n)*sum(x1*(y-y_pred))

        md2 = -(2/n)*sum(x2*(y-y_pred))
        md3= -(2/n)*sum(x3*(y-y_pred))

        md4 = -(2/n)*sum(x4*(y-y_pred))
        bd =-(2/n)*sum(y- y_pred)

        m1 = m1 - alpha*md1
        m2 = m2 - alpha*md2
        m3 = m3 - alpha*md3
        m4 = m4 - alpha*md4
        b = b - alpha*bd
        print(m1,m2,m3,m4,b,cost,i)


data  = pd.read_csv("Iris.csv")
x = data.iloc[:,0:5]
print(x)
x1 = x["SepalLengthCm"]
x2 = x["SepalWidthCm"]
x3 = x["PetalLengthCm"]
x4 = x["PetalWidthCm"]

y = data.iloc[:,5:6].values
print(y)
le = LabelEncoder()
y = le.fit_transform(y)

gradient_descent(x1,x2,x3,x4,y)