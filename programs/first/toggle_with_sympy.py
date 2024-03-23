from sympy import solve 
from sympy import Symbol
import numpy as np
x= Symbol("x", real = True)
k1=np.linspace(0,10,10)
k2=np.linspace(0,10,10)
multi=0
sol=[]
for i in k1:
    for j in k2:
        solutions=[]
        k= solve(x- i/(1+(j/(1+x**3))**3),x)
        print(k,i,j)
        for i in k:
            if i>0:
                solutions.append(i)
                if len(solutions)>1:
                    multi+=1
print(multi)