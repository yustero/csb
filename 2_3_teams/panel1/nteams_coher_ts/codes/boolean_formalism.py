# -*- coding: utf-8 -*-
"""
Created on Sat May 13 20:20:18 2023

@author: haldar
"""
## Library of various functions associated with boolean formalism
## Please refer to methods section of "Landscape of epithelial–mesenchymal plasticity as an emergent property of coordinated teams in regulatory networks", Kishore Hari et al.
import pandas as pd
import numpy as np
import random
import copy 

def parse_topo(filename): ##generates network as numpy matrix from TOPO.txt file
    topo_data = pd.read_csv("C:\\Users\\halda\\Downloads\\{}.topo.txt".format(filename), sep=" ").to_numpy() ##read topo data into pandas dataframe
    node_names = []
    node_id = []
    nid=0
    
    for i in range(0,len(topo_data)): 
        ## lists genes present in topo_data and assigns integer IDs to each
        if topo_data[i][0] not in node_names:
            node_names.append(topo_data[i][0])
            node_id.append(nid)
            nid=nid+1
            
        if topo_data[i][1] not in node_names:
            node_names.append(topo_data[i][1])
            node_id.append(nid)
            nid=nid+1
        
             
    node_to_id = dict(zip(node_names, node_id))
   ##converts gene names in topo_data to respective integer IDs         
    for i in range(len(topo_data)):
        topo_data[i][0] = node_to_id[topo_data[i][0]]
        topo_data[i][1] = node_to_id[topo_data[i][1]]

    n = len(node_names)  
    link_matrix = np.zeros((n, n))
    
    ##generates network from on topo_data
    for i in topo_data:
        link_matrix[i[0]][i[1]] = 1 if i[2] == 1 else -1
        
    
    adj = pd.DataFrame(link_matrix)
    NoInOut = False
    

    while NoInOut == False:
       ##deletion of any "peripheral nodes" (nodes with no incoming or no outgoing edges)
         outptLi = adj.loc[(adj==0).all(axis=1)].index
         notoutptLi = adj.loc[~(adj==0).all(axis=1)].index
         
         adj = adj.loc[notoutptLi, notoutptLi]
         
         inptLi = adj.loc[:, (adj==0).all(axis=0)].columns
         notinptLi = adj.loc[:, ~(adj==0).all(axis=0)].columns
         
         adj = adj.loc[notinptLi, notinptLi]
         
         if not (list(inptLi) + list(outptLi)):
             NoInOut = True
             break
   
    mat=adj.to_numpy()
               
    return mat, node_to_id, n


def update(state, link_matrix, pos): ##updates a chosen node in given network state using ising formalism
    mat=link_matrix.copy()
    n=len(state)
    updatepos=0
    summ=0
        
    for i in range (0,n):
        summ+=(mat[i][pos])*(state[i]) ##determines if node state agrees with ^incoming^ activations and inhibitions
            
    if summ>0:
        updatepos=1 ##turn node ON if activation>inhibition
    elif summ<0 :
        updatepos=-1 ##turn node OFF if activation<inhibition
    elif summ ==0:
        updatepos=state[pos] ##leave node as is if activation=inhibiton
    
    return updatepos

def issteady(state, link_matrix): ##checks if given network state is steady
    
    n=len(state)
    check=0
              
    for i in range(0,n):
        
        if state[i]!=update(state, link_matrix, i): ##checks if there are any nodes that can be updated
            check+=1
            break
        
    if check==0: ##state is steady if no nodes can be updated
        return True
    else:
        return False

            
def randomstate(lenmat): ##generate a random boolean state for a given network size

    state=[]
    
    for i in range (0,lenmat):
        x=random.randint(0,1)
        state.append(1) if x==1 else state.append(-1)
        
    return state

def randomnetwork(mat,swaps): ##create a new network from a given network by randomly swapping a given no. of pairs of edges
    count=0
    n=len(mat)
    randmat=mat.copy()
    while count<swaps: ##swap a given no. of edges
        i=random.randint(0,n-1)##randomly choose start point for 1st edge
        j=random.randint(0,n-1)##randomly choose end point for 1st edge
        x=random.randint(0,n-1)##randomly choose start point for 2nd edge
        y=random.randint(0,n-1)##randomly choose end point for 2nd edge
        if (randmat[i][j])*(randmat[x][y])==0: #check if both edges exist
            continue
        else:
            count+=1
            new=randmat[i][j]
            randmat[i][j]=randmat[x][y] ##swap edges if both exist
            randmat[x][y]=new
    
    return randmat


def initcond(lenmat,simno): #generates a set of initial states for simulation in a network
    instates=[]
    count=0
    while count<simno:
        state=randomstate(lenmat)
        
        instates.append(state)
        count+=1
    return instates
               
def sim(mat,init, includenonsteady): #uses asynchronous updating to simulate a given set of initial states in a network
    ststates=[]
    n=len(mat)
    instates=init.copy()
    for state in instates:
        
        for t in range (0,1000):
    
            if issteady(state,mat)==True:
                ststates.append(state) #record final steady state
                break
                
            else:
                pos=random.randint(0,n-1) #choose random node for updation if state isnt steady
                state[pos]=update(state,mat,pos) #update chosen node
            
            if t==999 and includenonsteady==True: #includes non-steady final states if desired
                ststates.append(state)
                

    return ststates

def deepsim(mat,init, includenonsteady): #same as sim but uses deepcopying instead
    ststates=[]
    n=len(mat)
    instates=copy.deepcopy(init)
    for state in instates:
        
        for t in range (0,1000):
    
            if issteady(state,mat)==True:
                ststates.append(state) #record final steady state
                break
                
            else:
                pos=random.randint(0,n-1) #choose random node for updation if state isnt steady
                state[pos]=update(state,mat,pos) #update chosen node
            
            if t==999 and includenonsteady==True: #includes non-steady final states if desired
                ststates.append(state)
                
    return ststates

def uniquestates(ststates): #counts the number of unique states for a given list of final states
    uniq_states=[]
    for i in ststates:
        if i not in uniq_states: 
            uniq_states.append(i)
    return uniq_states


def frustration(mat,state): #calculates frustration of a given steady state for a given network
    frus=0
    edges=0
    n=len(state)
    for i in range(n):
        for j in range(n):
            if mat[i][j]!=0:
                edges+=1
                
    for i in range(n):
        for j in range(n):
            if (mat[i][j])*state[i]*state[j]<0:
                frus+=1
                
    return frus/edges


def coherence(ststate,mat,n): #calc coherence of a state for n simultaneous perturbations
    coher=0
    for i in range(100):
        stcopy=ststate.copy()
        flipnodes=random.sample([a for a in range(len(ststate))], n) #choose nodes to flip
        for node in flipnodes:
            stcopy[node]=-stcopy[node] #flip nodes
        for i2 in range(10):
            instate=[]
            instate.append(stcopy)
            finstate=deepsim(mat,instate,True) #simuate perturbed initial state
            if ststate in finstate: #check if final=initial state
                coher+=1
    return(coher/1000)
                    
            
                











    
    
                    


        
        
    
    