import random 
import numpy as np 


#utility 
def indegree(adj,pos):
    n=len(adj)
    indeg=0
    for i in range(0,n):
        indeg+=abs(adj[i][pos])
    return(indeg)

def update(input,adj,pos):
    n=len(adj)
    adj_sum=0
    indeg=indegree(adj,pos)
    


    output=input.copy()

    for i in range(0,n):
        adj_sum+= (adj[i][pos]*input[i])

    drive=adj_sum/indeg

    if drive>0.5:
        output[pos] = 1

    if drive <= 0.5 and drive > 0: 
        output[pos]= 0.5

    if drive < 0 and drive >= -0.5:
        output[pos] = -0.5

    if drive < -0.5:
        output[pos] = -1
    
    if drive==0:
        output[pos]=0
    return(output)

def update_ising(nodes_state,adj,pos):
    
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


def steady_check(input,adj):
    n=len(adj)
    count=0
    for i in range(0,n):
        if update(input,adj,i)!= input:
            count+=1
    if count>0:
        return(False)
    if count==0:
        return(True)

def random_inputs(adj):
    n=len(adj)
    nodes_initial= [0 for i in range(0,n)]
    for i in range(n):
        k = random.choice([-1,0,1])
        nodes_initial[i]=k
    return(nodes_initial)

def sim(adj,numosim):
    n=len(adj)

    steady_states=[]

    for i in range(0,numosim):
        input = random_inputs(adj)
        time=0
        while True:
            rindex=random.randint(0,n-1)
            
            
            int_buff = update(input,adj,rindex)
            
            if steady_check(int_buff,adj):
                steady_states.append(int_buff)
                
                break
            else:
                input=int_buff
            
            time+=1
            if time==1000:
                break
    
    return(steady_states)





#ising formalism sim funciton
def sim2(adj,numosim):
    n=len(adj)

    steady_states=[]

    for i in range(0,numosim):
        input = random_inputs(adj)
        time=0
        while True:
            rindex=random.randint(0,n-1)
            
            
            int_buff = update_ising(input,adj,rindex)
            
            if steady_check(int_buff,adj):
                steady_states.append(int_buff)
                
                break
            else:
                input=int_buff
            
            time+=1
            if time==1000:
                break
    
    return(steady_states)












def ssf(steadys,adj):
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

adj=[[1,1,-1,-1],[1,1,-1,-1],[-1,-1,1,1],[-1,-1,1,1]]
adj2=[[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0], [1, 1, 1, -1, 0, 1, 0, 1, 0, -1, 0, 0, 0, 0, -1], [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, -1, 0, 0, -1, 0, 0], [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, -1, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, -1, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, -1, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, -1, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, -1, 0, -1, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0]]

steadys=sim(adj2,1000)
print(len(ssf(steadys,adj2)[1]))