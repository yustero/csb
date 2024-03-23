import random

def evolve(nodes_state,adj,pos):
    # Update the position as per 4 state model 
    #This is slightly inefficient since the indegree would always be calculated but i'll write it anyway for the first try 
    #Warning about nodes with 0 indegree 


    n=len(adj)
    adj_sum=0
    indeg=0
    buffer=nodes_state.copy()
    
    for i in range(0,n):
        indeg+= abs(adj[i][pos])


    for i in range(0,n):
        adj_sum+= (nodes_state[i]*adj[i][pos])
    


    

    if indeg!=0:
        
        drive=adj_sum/indeg        


        if drive>0.5:
            buffer[pos] = 1

        if drive <= 0.5 and drive > 0: 
            buffer[pos]= 0.5

        if drive < 0 and drive >= -0.5:
            buffer[pos] = -0.5

        if drive < -0.5:
            buffer[pos] = -1
        
        if drive==0:
            buffer[pos]=buffer[pos]
        

        return(buffer)

    else:
        raise Exception("0 indegree not allowed")

def evolve_turnoff(nodes_state,adj,pos):
    # Update the position as per 4 state model 
    #This is slightly inefficient since the indegree would always be calculated but i'll write it anyway for the first try 
    #Warning about nodes with 0 indegree 


    n=len(adj)
    adj_sum=0
    indeg=0
    buffer=nodes_state.copy()
    
    for i in range(0,n):
        indeg+= abs(adj[i][pos])


    for i in range(0,n):
        adj_sum+= (nodes_state[i]*adj[i][pos])
    


    

    if indeg!=0:
        
        drive=adj_sum/indeg        


        if drive>0.5:
            buffer[pos] = 1

        if drive <= 0.5 and drive > 0: 
            buffer[pos]= 0.5

        if drive < 0 and drive >= -0.5:
            buffer[pos] = -0.5

        if drive < -0.5:
            buffer[pos] = -1
        
        if drive==0:
            buffer[pos]=0
        

        return(buffer)

    else:
        raise Exception("0 indegree not allowed")

def steady_check(nodes,adj):
    n=len(adj)
    count=0
    for i in range(0,n):
        if evolve(nodes,adj,i)[i]!= nodes[i]:
           
           count+=1
        
    if count==0:
        return(True)
    else:
        return(False)


def random_inputs(adj):
    n=len(adj)
    nodes_initial= [0 for i in range(0,n)]
    for i in range(n):
        k = random.choice([-1,1])
        nodes_initial[i]=k
    return(nodes_initial)

def steady_states(adj,nodes, number_of_simulations):
    steadys=[]
    n=len(adj)    
    
    for i in range(number_of_simulations):
        nodes_state=random_inputs(adj).copy()
        t=0


        while True:
            k=random.randint(0,n-1)
            if k in nodes:
                 out = evolve_turnoff(nodes_state,adj,k)
            if k not in nodes:
                out=evolve(nodes_state,adj,k)
            if steady_check(out,adj):
                steadys.append(out)
                
                break
                
            else :
                nodes_state=out
                
            
            t+=1
            if t==1000:
                break
    return(steadys)