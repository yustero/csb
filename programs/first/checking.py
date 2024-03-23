import numpy as np
from scipy.integrate import odeint, solve_ivp
from scipy.optimize import root_scalar, root, fsolve
import matplotlib.pyplot as plt
import warnings

def constants(var):
    def func(x):
        return([x[0]-(var[0]/(1+x[1])), x[1]-(var[1]/(1+x[0]))])
    return func

'''var=[0,0]
k1=np.linspace(1,10)

k2=np.linspace(1,10)

def solution_counter(var):
    solutions=[]
    dsolutions=[]
    for l in np.linspace(0,var[0]):
        for m in np.linspace(0,var[1]):
            solutions.append(fsolve(constants([var[0],var[1]]),[l,m]))
    for i in solutions:
        if i[0]>0 and i[1]>0:
            dsolutions.append(i)
            break


    for i in range(0,len(solutions)):
        if abs(solutions[i][0] - dsolutions[0][0]) > 0.001 and abs(solutions[i][1] - dsolutions[0][1])>0.001 and solutions[i][0]>0 and solutions[i][1]>0:
            dsolutions.append(solutions[i])

    return(len(dsolutions),dsolutions)

print(solution_counter([2.10,6.69]))
print(solution_counter([7.06,2.10]))'''
sol=[]
try:
    warnings.warn(Warning())
    k=fsolve(constants([7.06,2.10]),[1.296,1.757])
    sol.append(k)
except Warning:
    pass
print(k)