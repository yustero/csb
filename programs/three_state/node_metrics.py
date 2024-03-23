import numpy as np
import random
import randomization
import coherent_parser
import copy

def adj_summary(adj):
    nodes=len(adj)
    n=nodes
    edges=0
    pedges=0
    nedges=0
    for i in range(0,n):
        for j in range(0,n):
            if adj[i][j]==1:
                pedges+=1
                edges+=1
            if adj[i][j]==-1:
                nedges+=1
                edges+=1
    return(nodes,edges,pedges,nedges)





def adj_reduction(adj,nodes):
    n=len(adj)
    mat=[]
    for i in range(0,n):
        if i in nodes:
            edge=[]
            for j in range(0,n):
                if i in nodes and j in nodes:
                    edge.append(adj[i][j])
            mat.append(edge)
    return(mat)





def impurity_test(adj,t1,t2):
    #To see if it has impurities or not
    n=len(adj)

    for i in range(0,n):
        for j in range(0,n):
            if i< t1 and j<t1:
                if adj[i][j]==-1:
                    return False 
            if i>=t1 and j>= t1:
                if adj[i][j]==-1:
                    return(False)

            if i >=t1 and j < t1:
                if adj[i][j]==1:
                    return(False)
            if i <t1 and j >= t1:
                if adj[i][j]==1:
                    return(False)

def impurity_list(adj,t1,t2):
    #To get a list of impurities if any
    n=len(adj)
    impurities=[]
     
    for i in range(0,n):
        for j in range(0,n):
            
            if i< t1 and j<t1:
                if adj[i][j]==-1:
                    impurities.append([i,j]) 
            if i>=t1 and j>= t1:
                if adj[i][j]==-1:
                    impurities.append([i,j])

            if i >=t1 and j < t1:
                if adj[i][j]==1:
                    impurities.append([i,j])

            if i <t1 and j >= t1:
                if adj[i][j]==1:
                    impurities.append([i,j])

    return(impurities)

def purify(adj,t1,t2):
    n=len(adj)
    impurities=[]

    pure_mat=copy.deepcopy(adj)


    for i in range(0,n):
        for j in range(0,n):
            
            if i< t1 and j<t1:
                if adj[i][j]==-1:
                    impurities.append([i,j])
                    pure_mat[i][j]=1 
            
            if i>=t1 and j>= t1:
                if adj[i][j]==-1:
                    impurities.append([i,j])
                    pure_mat[i][j]=1

            if i >=t1 and j < t1:
                if adj[i][j]==1:
                    impurities.append([i,j])
                    pure_mat[i][j] = -1
            
            if i <t1 and j >= t1:
                if adj[i][j]==1:
                    impurities.append([i,j])    
                    pure_mat[i][j] = -1 
    return(pure_mat)

def node_knockout(adj,nodes):
    n=len(adj)
    nodesp=[]
    for i in range(0,n):
        if i not in nodes:
            nodesp.append(i)

    mat=adj_reduction(adj,nodesp)
    return(mat)




def node_flip(state,node):
    output=state.copy()
    output[node]=output[node]*-1
    return(output)







def indegree(adj):
    n=len(adj)
    indeg=[]
    for i in range(0,n):
        count=0
        for j in range(0,n):
            if adj[j][i]==1 or adj[j][i]==-1:
                count+=1
        indeg.append(count)
    return(indeg)

def outdegree(adj):
    n=len(adj)
    outdeg=[]
    for i in range(0,n):
        count=0
        for j in range(0,n):
            if adj[i][j]==1 or adj[i][j]==-1:
                count+=1
        outdeg.append(count)
    return(outdeg)

def indeg_summary(adj):
    n=len(adj)
    indeg=[]
    posd=[]
    negd=[]
    can=[]
    for i in range(0,n):
        count=0
        pos=0
        neg=0
        for j in range(0,n):
            if adj[j][i]==1 or adj[j][i]==-1:
                count+=1
            if adj[j][i]==1:
                pos+=1
            if adj[j][i]==-1:
                neg+=1
        posd.append(pos)
        negd.append(neg)
        can.append(abs(pos-neg))
        
        indeg.append(count)
    norm_incan=[]
    for i in range(0,n):
        if indeg[i]!=0:
            norm_incan.append(can[i]/indeg[i])
        else:
            norm_incan.append(0)
    return(can,posd,negd,indeg, np.mean(can),norm_incan)

def influence_static_can(adj):
    n=len(adj)
    indeg=[]
    posd=[]
    negd=[]
    can=[]
    
    infmat=coherent_parser.influence_matrix(adj)


    for i in range(0,n):
        count=0
        pos=0
        neg=0
        for j in range(0,n):
            
            if infmat[j][i]>0:
                pos+=infmat[j][i]
            if infmat[j][i]<0:
                neg+=infmat[j][i]
        posd.append(pos)
        negd.append(neg)
        can.append(abs(pos-neg))
        
        
    return(can,posd,negd, np.mean(can))

    
    





def outdeg_summary(adj):
    n=len(adj)
    outdeg=[]
    posd=[]
    negd=[]
    can=[]
    for i in range(0,n):
        count=0
        pos=0
        neg=0
        for j in range(0,n):
            if adj[i][j]==1 or adj[i][j]==-1:
                count+=1
            if adj[i][j]==1:
                pos+=1
            if adj[i][j]==-1:
                neg+=1
        posd.append(pos)
        negd.append(neg)
        can.append(abs(pos-neg))
        
        outdeg.append(count)
    return(can,posd,negd,outdeg, np.mean(can))




def edge_breakdown(adj):
    n=len(adj)
    dat= coherent_parser.clustered_matrix_adj(adj)
    t1=dat[1]
    t2=dat[2]

    toted=0
    
    allmax=n**2
    t1emax=t1**2
    t2emax=t2**2
    t1t2emax=t1*t2
    t2t1emax=t1*t2

    t1e=0
    t2e=0
    t1t2e=0
    t2t1e=0


    for i in range(0,n):
        for j in range(0,n):
            if adj[i][j]!=0:
                toted+=1

            if i<t1 and j < t1:
                if adj[i][j]!=0:
                    t1e+=1
            
            if i>=t1 and j>=t1:
                if adj[i][j]!=0:
                    t2e+=1
            
            if i<t1 and j>=t1:
                if adj[i][j]!=0:
                    t1t2e+=1

            if i>=t1 and j<t1:
                if adj[i][j]!=0:
                    t2t1e+=1
    edgeval=[toted,t1e,t2e,t1t2e,t2t1e]
    edge_density=[toted/allmax, t1e/t1emax,t2e/t2emax,t1t2e/t1t2emax, t2t1e/t2t1emax]
    return(edgeval,edge_density)

def state_node_sum(adj,state):
    n=len(adj)
    sumd=[]
    for i in range(0,n):
        sum=0
        for j in range(0,n):
            sum+=state[j]*adj[j][i]
        sumd.append(sum)
    return(sumd)

def abs_state_node_sum(adj,state):
    abssumd=[]
    sumd=state_node_sum(adj,state)
    for i in sumd:
        abssumd.append(abs(i))
    return(abssumd)


def possible_canalising_strength_triple(adj, no_val):
    n=len(adj)
    cansd=[]
    def random_input(n):
        state=[0 for i in range(0,n)].copy()
    
        for i in range(0,n):
            state[i]=random.choice([-1,1])
        return(state)

    for i in range(0,no_val):
        inp=random_input(n)
        
        cansd.append(state_node_sum(adj,inp))
    
    return(cansd)

def high_team_strength(adj,number_sims,nedges):
    #wild type team_strength
    datawt=coherent_parser.clustered_matrix_adj(adj)
    mat=datawt[0]
    t1_wt=datawt[1]
    t2_wt=datawt[2]
    ts_wt=coherent_parser.rand_team_strength_rand(mat,t1_wt,t2_wt)
    
    
    
    high_team_mat=[]
    for i in range(0,number_sims):
        rand_mat=randomization.random_edge_exchange(adj,nedges)
        data=coherent_parser.clustered_matrix_adj(rand_mat)
        clust_rand_mat=data[0]
        t1=data[1]
        t2=data[2]
        ts_random=coherent_parser.rand_team_strength_rand(clust_rand_mat,t1,t2)
        if ts_random>ts_wt:
            high_team_mat.append(clust_rand_mat)
    
    return(high_team_mat)