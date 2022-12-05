import numpy as np
import pandas as pd


def train(feature,target):
    specific_hypo=feature[0].copy()
    general_hypo=np.full((len(feature[0]),len(feature[0])),fill_value='?',dtype=object)
    for i, f in enumerate(feature):
        if target[i]=="yes":
            for j, h in enumerate(specific_hypo):
                if h!=f[j]:
                    specific_hypo[j]="?"
                    general_hypo[j][j]="?"
        else:
            for j,h in enumerate(specific_hypo):
                if h!=f[j]:
                    general_hypo[j][j]=specific_hypo[j]
                else:
                    general_hypo[j][j]='?'

    check=np.full(len(specific_hypo),fill_value='?',dtype=object)
    indices=[]
    for i in range(len(general_hypo)):
        if np.array_equal(general_hypo[i],check):
            indices.append(i)
    general_hypo=np.delete(general_hypo,indices,axis=0)
    return general_hypo,specific_hypo


data=pd.read_csv("a1.csv")
feature=np.array(data)[:,:-1]
target=np.array(data)[:,-1]
print(feature)
print(target)
general_hypo,specific_hypo=train(feature,target)
print(specific_hypo)
print(general_hypo)