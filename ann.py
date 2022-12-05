import numpy as np
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([0.92], [0.86], [0.89]), dtype=float)
X = X/np.amax(X,axis=0) # maximum of X array longitudinally y = y/100

def sigmoid (x):
    return (1/(1 + np.exp(-x)))

def derivatives_sigmoid(x):
    return x * (1 - x)

epoch=7000
lr=0.1
inputNeurons = 2
hiddenNeurons = 3
outputNeurons = 1
wh=np.random.uniform(size=(inputNeurons,hiddenNeurons))
bh=np.random.uniform(size=(1,hiddenNeurons))
wout=np.random.uniform(size=(hiddenNeurons,outputNeurons))
bout=np.random.uniform(size=(1,outputNeurons))
for i in range(epoch):
    hinp1=np.dot(X,wh)
    hinp=hinp1 + bh
    hlayer_act = sigmoid(hinp)

    outinp1=np.dot(hlayer_act,wout)
    outinp= outinp1+ bout
    output = sigmoid(outinp)
    
    EO = y-output
    outgrad = derivatives_sigmoid(output)
    d_output = EO* outgrad
    
    EH = d_output.dot(wout.T)
    hiddengrad = derivatives_sigmoid(hlayer_act)
    d_hiddenlayer = EH * hiddengrad
    
    wout += hlayer_act.T.dot(d_output) *lr
    bout += np.sum(d_output, axis=0,keepdims=True) *lr
    
    wh += X.T.dot(d_hiddenlayer) *lr
    bh += np.sum(d_hiddenlayer, axis=0,keepdims=True) *lr
print("Input: \n" + str(X))
print("Actual Output: \n" + str(y))
print("Predicted Output: \n" ,output)
