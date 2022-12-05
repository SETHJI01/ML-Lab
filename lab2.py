import numpy as np 
import pandas as pd

records = pd.read_csv('a1.csv')
concepts = np.array(records.iloc[:,0:-1])
print("\nInstances are:\n",concepts)
target = np.array(records.iloc[:,-1])
print("\nTarget Values are: ",target)

def learning(concepts, target): 
    specific_hypothesis = concepts[0].copy()
    print("\nInitialization of specific_hypothesis and genearal_hypothesis")
    print("\nSpecific Boundary: ", specific_hypothesis)
    general_hypothesis = [["?" for i in range(len(specific_hypothesis))] for i in range(len(specific_hypothesis))]
    print("\nGeneric Boundary: ",general_hypothesis)  

    for i, h in enumerate(concepts):
        print("\nInstance", i+1 , "is ", h)
        if target[i] == "yes":
            print("Instance is Positive ")
            for x in range(len(specific_hypothesis)): 
                if h[x]!= specific_hypothesis[x]:                    
                    specific_hypothesis[x] ='?'                     
                    general_hypothesis[x][x] ='?'
                   
        else:            
            print("Instance is Negative ")
            for x in range(len(specific_hypothesis)): 
                if h[x]!= specific_hypothesis[x]:                    
                    general_hypothesis[x][x] = specific_hypothesis[x]                
                else:                    
                    general_hypothesis[x][x] = '?'        
        
        print("Specific Bundary after ", i+1, "Instance is ", specific_hypothesis)         
        print("Generic Boundary after ", i+1, "Instance is ", general_hypothesis)
        print("\n")

    indices = [i for i, val in enumerate(general_hypothesis) if val == ['?', '?', '?', '?', '?', '?']]    
    for i in indices:   
        general_hypothesis.remove(['?', '?', '?', '?', '?', '?']) 
    return specific_hypothesis, general_hypothesis 

specific_final, general_final = learning(concepts, target)

print("Final Specific_hypothesis: ", specific_final, sep="\n")
print("Final General_hypothesis: ", general_final, sep="\n")