import glob
#import numpy as np
import random
import Parser
import boolean_formalism_kushal


def evol(nodes_state,adj,pos):
    n = len(adj)
    adj_sum=0
    buffer=nodes_state.copy()
    for i in range(0,n):
        adj_sum+= (nodes_state[i]*adj[i][pos])
    if adj_sum>0:
        buffer[pos]=1
        
    
    elif adj_sum<0:
        buffer[pos]=-1
        
    elif adj_sum==0:
        buffer[pos]=buffer[pos]
    return(buffer)

def steady_check(nodes,adj):
    n= len(adj) 
    nn=nodes
    count=0
    for i in range(0,n):
        nodes=nn
        if evol(nodes,adj,i)[i]!= nodes[i]:
           print(evol(nodes,adj,i),nodes, "different")
           count+=1
        else:
            print(evol(nodes,adj,i),nodes,"sames1")
    if count==0:
        return(True)
    else:
        return(False) 

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
    lm = updatepos
    
    return(updatepos)



def steady_check2(nodes,adj):
    n= len(adj) 
    count=0
    for i in range(0,n):
        if update2(nodes,adj,i)!= nodes[i]:
           print(update2(nodes,adj,i),i,nodes, "differents2")           
           count+=1
        else:
           print(update2(nodes,adj,i),i,nodes, "sames2")            
    if count==0:
        return(True)
    else:
        return(False) 

def evol23(nodes_state,adj,pos):
    n = len(adj)
    adj_sum=0
    uffer=nodes_state
    for i in range(0,n):
        adj_sum+= (nodes_state[i]*adj[i][pos])
    if adj_sum>0:
        uffer[pos]=1
        
    
    elif adj_sum<0:
        uffer[pos]=-1
        
    elif adj_sum==0:
        uffer[pos]=uffer[pos]
    return(uffer)




topofiles_path= glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/landscape_of_epithelial_mesenchymal_paper/teams_data/Teams-main/TopoFiles/*topo")
topofiles=[x.split("/")[-1] for x in topofiles_path]
adj= Parser.adj_extract(topofiles[1])

store=[1, -1, -1, -1, 1, -1, 1, 1]
ss=[[1, -1, 1, -1, -1, -1, 1, 1], [1, -1, -1, -1, 1, -1, 1, 1], [-1, 1, -1, 1, 1, 1, -1, -1], [1, -1, -1, -1, 1, 1, 1, 1], [-1, 1, 1, 1, -1, -1, -1, -1], [-1, 1, 1, 1, 1, -1, -1, -1], [1, -1, -1, -1, -1, 1, 1, 1], [-1, 1, 1, 1, -1, 1, -1, -1], [-1, 1, 1, 1, 1, 1, -1, -1], [1, -1, -1, -1, -1, -1, 1, 1]]
print(ss[1])
print(steady_check2(ss[1],adj))
steady_check(ss[1],adj)

print(evol23(ss[1],adj,2),ss[1], "final")
print(store)