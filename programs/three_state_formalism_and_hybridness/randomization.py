import boolean_sim
import random
import numpy as np
import copy
import coherent_parser
import glob
import matplotlib.pyplot as plt
'''def random_edge_exchange(adj,k):
    n=len(adj)
    
    random_adj=copy.deepcopy(adj)
    rand2=copy.deepcopy(adj)
    
    for i in range(0,k):
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
        c=random.randint(0,n-1)
        d=random.randint(0,n-1)
        buffer= rand2[c][d]  
        random_adj[c][d]=  rand2[a][b]
        rand2[a][b] = buffer
    
    return(rand2)'''

def random_edge_exchange(adj,k):
    n=len(adj)
    
    random_adj=copy.deepcopy(adj)
    rand2=copy.deepcopy(adj)
    i=0
    while i<k:
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
        c=random.randint(0,n-1)
        d=random.randint(0,n-1)
        if rand2[a][b]*rand2[c][d]==-1:
            i+=1
            buffer= rand2[c][d]  
            rand2[c][d]=  rand2[a][b]
            rand2[a][b] = buffer
        
    return(rand2)

def edge_deletions(adj,k):
    n=len(adj)
    rand2=copy.deepcopy(adj)
    i=0
    while i<k:
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
        if rand2[a][b]!=0:
            rand2[a][b]=0
            i+=1 
    return(rand2)


def edge_inversion(adj,k):
    n=len(adj)
    rand2=copy.deepcopy(adj)
    i=0
    while i<k:
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
        if rand2[a][b]!=0:
            rand2[a][b]=rand2[a][b]* (-1)
            i+=1 
    return(rand2)



def edge_change(adj,k):
    n=len(adj)
    
    random_adj=copy.deepcopy(adj)
    rand2=copy.deepcopy(adj)
    i=0
    while i<k:
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
        c=random.randint(0,n-1)
        d=random.randint(0,n-1)
        if rand2[a][b]*rand2[c][d]==0:
            i+=1
            buffer= rand2[c][d]  
            rand2[c][d]=  rand2[a][b]
            rand2[a][b] = buffer
        
    return(rand2)
    
#Completely random matrices
def random_matrix_generator(n):
    val=[-1,0,1]
    mat=[]
    for i in range(0,n):
        edge=[]
        for j in range(0,n):
            edge.append(random.choice(val))
        mat.append(edge)
    return(mat)

def rand_mat_n_e(n,e):
    edges=[0 for i in range(0,n)]
    mat=[edges.copy() for i in range(0,n)]
    i=0
    
    while i< e:
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
        if mat[a][b]==0:
            val =random.choice([-1,1])
            mat[a][b]= val
            i+=1
    return(mat)


