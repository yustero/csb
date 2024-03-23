import Parser
import numpy as np
import boolean_simulation
import pandas as pd
import glob
import csv
import random 
import matplotlib.pyplot as plt
import boolean_formalism_kushal


def random_inputs(adj):
    nodes_initial=[]
    for i in range(len(adj)):
        k = random.choice([-1,1])
        nodes_initial.append(k)
    return(nodes_initial)


def update2(state, link_matrix, pos): 
    grr=state
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
    state[pos]=updatepos
    return(updatepos)

def evol(nodes_state,adj,pos):
    n = len(adj)
    adj_sum=0
    for i in range(0,n):
        adj_sum+= (nodes_state[i]*adj[i][pos])
    if adj_sum>0:
        nodes_state[pos]=1
        
    
    elif adj_sum<0:
        nodes_state[pos]=-1
        
    elif adj_sum==0:
        nodes_state[pos]=nodes_state[pos]
    return(nodes_state)

def evol2(nodes_state,adj,pos):
    n = len(adj)
    adj_sum=0
    for i in range(0,n):
        adj_sum+= (nodes_state[i]*adj[i][pos])
    if adj_sum>0:
        nodes_state[pos]=1
        
    
    elif adj_sum<0:
        nodes_state[pos]=-1
        
    elif adj_sum==0:
        nodes_state[pos]=nodes_state[pos]
    return(nodes_state[pos])



def steady_check(nodes,adj):
    n= len(adj) 
    count=0
    for i in range(0,n):
        if update2(nodes,adj,i)!= nodes[i]:
           
           count+=1
        
    if count==0:
        return(True)
    else:
        return(False) 

def steady_states(adj, number_of_simulations):
    steadys=[]
    n=len(adj)    
    
    for i in range(number_of_simulations):
        nodes_state=random_inputs(adj)
        t=0
        while True:
            k=random.randint(0,n-1)
            
            out = evol(nodes_state,adj,k)
            if steady_check(out,adj):
                if out not in steadys:
                    steadys.append(out)
                    break
                else:
                    break
            else :
                nodes_state=out
            
            t+=1
            if t==1000:
                break
    return(steadys)

def uniquestates(ststates):
    uniq_states=[]
    for i in range(0, len(ststates)):
        if ststates[i] not in uniq_states:
            uniq_states.append(ststates[i])
    return uniq_states
topofiles_path= glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/landscape_of_epithelial_mesenchymal_paper/teams_data/Teams-main/TopoFiles/*topo")
topofiles=[x.split("/")[-1] for x in topofiles_path]
file=topofiles[1]
adj = Parser.adj_extract(file)
print(file)

print(len(steady_states(adj,1000)))

for i in (steady_states(adj,100)):
    print(boolean_formalism_kushal.issteady(i,adj))
    
    print(steady_check(i,adj))

    print("----")
print(adj)
print(steady_states(adj,1000))