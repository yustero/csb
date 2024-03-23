
import random
import numpy as np

def evolve_ising(nodes_state,adj,pos):
    
    n=len(adj)
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


def random_inputs(adj):
    n=len(adj)
    nodes_initial= [0 for i in range(0,n)]
    for i in range(n):
        k = random.choice([-1,1])
        nodes_initial[i]=k
    return(nodes_initial)

def steady_check(nodes,adj):
    n=len(adj)
    count=0
    for i in range(0,n):
        if evolve_ising(nodes,adj,i)[i]!= nodes[i]:
           
           count+=1
        
    if count==0:
        return(True)
    else:
        return(False)

def steady_states(adj, number_of_simulations):
    steadys=[]
    n=len(adj)    
    
    for i in range(number_of_simulations):
        nodes_state=random_inputs(adj).copy()
        t=0
        timedist=[]
        timtaken=0
        while True:
            k=random.randint(0,n-1)
            
            out = evolve_ising(nodes_state,adj,k)
            if steady_check(out,adj):
                steadys.append(out)
                timedist.append(timtaken)
                timtaken=0
                break
                
            else :
                nodes_state=out
                timtaken+=1
            
            t+=1
            if t==1000:
                break
    return(steadys)


def input_steady(nodes_input,adj):
    #This function takes in input and subjects it to ising formalism and then returns a list with the outcome state instead of the state directly so if the list is empty then steady state wasn't reached
    
    steadys=[]
    n=len(adj)    
    
    
    nodes_state=nodes_input.copy()
    t=0
    while True:
        k=random.randint(0,n-1)
        
        out = evolve_ising(nodes_state,adj,k)
        if steady_check(out,adj):
            steadys.append(out)
            break
            
        else :
            
            nodes_state=out
        
        t+=1
        if t==1000:
            break
    return(steadys)  






def steady_state_frequency(steadys,adj):
    
    n=len(adj)
    sf=[[],[]]
    stn=len(steadys)
    for i in range(0,stn):
        if steadys[i] not in sf[0]:
            sf[0].append(steadys[i])
            sf[1].append(1)
        elif steadys[i] in sf[0]:
            m=sf[0].index(steadys[i])
            sf[1][m]+=1
    return(sf)


def frustration(state,adj):
    n=len(adj)
    frust=0
    for i in range(0,n):
        for j in range(0,n):
            frust+=state[i]*state[j]*adj[i][j]
    return(frust)
def mean_frustration(steadystates,adj):
    frust_dsit=[]
    for i in steadystates:
        frust_dsit.append(frustration(i,adj))
    return(np.mean(frust_dsit))