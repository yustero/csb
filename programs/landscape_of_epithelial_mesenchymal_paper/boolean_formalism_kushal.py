# -*- coding: utf-8 -*-
"""
Created on Sat May 13 20:20:18 2023

@author: haldar
"""
import Parser
import glob
import pandas as pd
import numpy as np
import random
import boolean_simulation


def parse_topo(filename): #simplified from original csbbsse code ; no longer requires a separate ids file
    topo_data = pd.read_csv("C:\\Users\\halda\\Downloads\\{}.topo.txt".format(filename), sep=" ").to_numpy()
    node_names = []
    node_id = []
    nid=0
    
    for i in range(0,len(topo_data)):
        
        if topo_data[i][0] not in node_names:
            node_names.append(topo_data[i][0])
            node_id.append(nid)
            nid=nid+1
            
        if topo_data[i][1] not in node_names:
            node_names.append(topo_data[i][1])
            node_id.append(nid)
            nid=nid+1
               
    node_to_id = dict(zip(node_names, node_id))
    
    for i in range(len(topo_data)):
        topo_data[i][0] = node_to_id[topo_data[i][0]]
        topo_data[i][1] = node_to_id[topo_data[i][1]]

    n = len(node_names)  
    link_matrix = np.zeros((n, n))
    
    for i in topo_data:
        link_matrix[i[0]][i[1]] = 1 if i[2] == 1 else -1

    return link_matrix, node_to_id


def update(state, link_matrix, pos): 
    
    n=len(state)
    updatepos=0
    summ=0
        
    for i in range (0,n):
        summ+=(link_matrix[i][pos])*(state[i])
            
    if summ>0:
        updatepos=1
    elif summ<0 :
        updatepos=-1 
    elif summ ==0:
        updatepos=state[pos]
    
    return updatepos

def issteady(state, link_matrix): 
    
    n=len(state)
    check=0
              
    for i in range(0,n):
        
        if state[i]!=update(state, link_matrix, i):
            check+=1
            break
        
    if check==0:
        return True
    else:
        return False

            
def randomstate(link_matrix):
    
    n=len(link_matrix)
    state=[]
    
    for i in range (0,n):
        a=random.randint(0,1)
        state.append(1) if a==1 else state.append(-1)
        
    return state

def randomnetwork(mat):
    count=0
    n=len(mat)
    randmat=mat.copy()
    while count<10:
        i=random.randint(0,n-1)
        j=random.randint(0,n-1)
        x=random.randint(0,n-1)
        y=random.randint(0,n-1)
        if (randmat[i][j])*(randmat[x][y])==0:
            continue
        else:
            count+=1
            new=randmat[i][j]
            randmat[i][j]=randmat[x][y]
            randmat[x][y]=new
    
    return randmat
        
def sim(mat,simno):
    
    n=len(mat)
    edges=0
    for i in range (0,n):
        for j in range (0,n):
            if mat[i][j]!=0:
                edges+=1

    instates=[]
    ststates=[]
    count=0

    while count<simno:
        state=randomstate(mat)

        if state in instates:
            continue
        else:
            instates.append(state)
            count=count+1

            for t in range (0,1000):
    
                if issteady(state,mat)==True:
                    ststates.append(state)
                    break
                
                else:
                    pos=random.randint(0,n-1)
                    state[pos]=update(state,mat,pos)

    return n,edges,ststates

def uniquestates(ststates):
    uniq_states=[]
    for i in range(0, len(ststates)):
        if ststates[i] not in uniq_states:
            uniq_states.append(ststates[i])
    return uniq_states
'''    

topofiles_path= glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/landscape_of_epithelial_mesenchymal_paper/teams_data/Teams-main/TopoFiles/*topo")
topofiles=[x.split("/")[-1] for x in topofiles_path]

adj=Parser.adj_extract(topofiles[0])
print(topofiles[0])

k=sim(adj,10000)

print(len(uniquestates(k[0])))
'''