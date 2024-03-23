import numpy as np
from scipy.optimize import brentq,fsolve

def constants(var):

    def func(x):
        return(x- var[0]/(1+var[1]/(1+x)))
    return(func)
var=[0,0]
k1= np.linspace(0,10)

k2= np.linspace(0,10)
multistab=0
for i in k1:
    for j in k2:
        solutions=[]
        var[0]=i
        var[1]=j
        solutions.append(brentq(constants(var),a=0.001,b=100))
        
        for m in np.linspace(0,100):
            k=brentq(constants(var),a=m,b=100)
            for i in solutions:
                if abs(k-i)>0.01:
                    solutions.append(k)
