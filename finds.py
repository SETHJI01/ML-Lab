import numpy as np
import pandas as pd
data=pd.read_csv("a1.csv")
print(data)
c=np.array(data)[:,:-1]
t=np.array(data)[:,-1]
print(c)
print(t)

def train(c,t):
    for i, val in enumerate(t):
        if(val=="yes"):
            specific_hypothesis=c[i].copy()
            break
    for i, ch in enumerate(c):
        if(t[i]=="yes"):
            for j in range(len(specific_hypothesis)):
                if(specific_hypothesis[j]==ch[j]):
                    pass
                else:
                    specific_hypothesis[j]="?"
        else:
            pass
    return specific_hypothesis
print(train(c,t))