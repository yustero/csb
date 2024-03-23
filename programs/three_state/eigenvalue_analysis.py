'''My hypothesis is that more the dimensionality of the eigenspace, the more the number of different solutions you get via formalism, there should be some correlation between the number of eigenvalues and number of solutions you get'''
import numpy as np
import randomization
import random
import matplotlib.pyplot as plt 
import coherent_parser
import artificial 




def dim_eigenspace(adj):
    count=0
    for i in np.linalg.eig(adj)[0]:
        if i>= 1 and i.imag==0:
            count+=1
    return(count)

def dist_eigenspace(matrices):
    dist=[]
    for i in matrices:
        dist.append(dim_eigenspace(i))

