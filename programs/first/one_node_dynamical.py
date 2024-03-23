import numpy as np
from scipy.integrate import odeint, solve_ivp
from scipy.optimize import root_scalar, root, fsolve, brentq
import matplotlib.pyplot as plt


def constants(var):
    def func(x):
        return([x[0]-(var[0]/(1+x[1])), x[1]-(var[1]/(1+x[0]))])
    return func

var=[0,0]
k1=np.linspace(1,10)

k2=np.linspace(1,10)
'''
def solution_counter(var):
    solutions=[]

    for l in np.linspace(0,var[0]):
        for m in np.linspace(0,var[1]):
            solutions.append(fsolve(constants([var[0],var[1]]),[l,m]))
    dsolutions=[solutions[0]]
    for i in range(1,len(solutions)):
        if abs(solutions[i][0] - solutions[0][0]) > 0.001 and abs(solutions[i][1] - solutions[0][1])>0.001:
            dsolutions.append(solutions[i])
    return(len(dsolutions))

print(solution_counter([3,10]))
'''
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

    return(len(dsolutions))



multistable=0
number_of_parameters=0
for i in k1:
    for j in k2:
        var[0]=i
        var[1] =j
        solc=solution_counter(var)
        print(solc,var[0],var[1])
        number_of_parameters+=1    
        if  solc >1 :
            multistable+=1
        
print(multistable,number_of_parameters)
        
'''        for l in np.linspace(0,i):
            for m in np.linspace(0,j):
                solution = fsolve(constants([var[0],var[1]]), [l,m])
                print(solution)
'''