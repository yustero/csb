import coherent_parser 
import numpy as np
import topopath
import random 

k=2
network=coherent_parser.clustered_matrix_file(topopath.topofiles[k])
adj=network[0]

def same_sign(state,adj):
    n=len(adj)
    t1=[]
    t2=[]
    for i in range(0,n):
        if state[i]>0:
            t1.append(i)
        if state[i]<0:
            t2.append(i)
    return(t1,t2)

def random_input(adj):
    n=len(adj)

    rand_int=[]
    for i in range(0,n):
        rand_int.append(random.choice([-1,1]))
    return(rand_int)


mat=[]
for i in adj:
    mat.append(np.array(i))
np.array(mat)
print(mat)

pow_mat=np.linalg.matrix_power(mat,10)

'''while True:
    input=random_input(adj)    
    print(same_sign(np.matmul(pow_mat,input),adj))
'''
print(network[-1][21])