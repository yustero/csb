import random 
import copy
import numpy as np 




def team_ranges(teamsizes):
    
    trange=[0]
    nteams=len(teamsizes)
    for i in range(1,nteams+1):
        trange.append(trange[i-1]+teamsizes[i-1])
    #The last entry in the list indicates the total of nodes in the network
    return(trange)


def edge_sign_teams(trange,i,j):
    #i,j belong to the adjacency matrix
    #This function takes a random i,j value from the adjacency matrix and tells us whether in an ideal network of nteams the egde should be +1 or -1
    # let's denote by l and m the interaction between i'th team and j'th team 
    #Now this program assumes that the values of i and j are reasonable and do not exceed their max possible value via adjacency matrix
    #Notice how p and q are used to index through the lists.

    count1=0
    ninterval=len(trange)-1

    for p in range(0,ninterval):
        if i>= trange[p] and i < trange[p+1]:
            l=count1
            break
        else:
            count1+=1
    count2=0
    for p in range(0,ninterval):
        if j>= trange[p] and j < trange[p+1]:
            m=count2
            break
        else:
            count2+=1
    if l==m:
        return(1,l,m)
    if l!=m:
        return(-1,l,m)


def edge_exhaust(edge_mat):
    #This function tells if the edge matrix has been exhausted
    count=0
    n=len(edge_mat)
    for i in range(0,n):
        for j in range(0,n):
            if edge_mat[i][j]!=0:
                count+=1
    if count>0:
        return(False)
    if count ==0:
        return(True)

def nteam_net(n,teamsizes,densities):
    #teamsizes is a list having all the teamsizes
    #n is the number of teams



    if len(teamsizes)!=n or len(densities)!=n:
        raise ValueError
    
    trange=team_ranges(teamsizes)

    num_nodes=0
    for i in teamsizes:
        num_nodes+=i
    
    
    edge_mat=[]
    
    for i in range(0,n):
        edge_mat.append([])
        for j in range(0,n):
            edge_mat[i].append(np.floor(densities[i][j]*teamsizes[i]*teamsizes[j]))
    
    edge_mat_exhaust=copy.deepcopy(edge_mat)


    adjedge=[0 for i in range(0,num_nodes)]
    adj=[adjedge.copy() for i in range(0,num_nodes)]
    
    if edge_exhaust(edge_mat_exhaust)==True:
        return([adj])
    while edge_exhaust(edge_mat_exhaust)==False:
        i = random.randint(0,num_nodes-1)
        j = random.randint(0,num_nodes-1)
        data_edge=edge_sign_teams(trange,i,j)
        
        
        edge_sign=data_edge[0]
        
        l=data_edge[1]
        m=data_edge[2]
        
        
        if edge_mat_exhaust[l][m]!=0 and adj[i][j]==0:
            adj[i][j]=edge_sign
            edge_mat_exhaust[l][m]+=-1
    #We construct a nxn matrix having different number of different types of edges. 
        if edge_exhaust(edge_mat_exhaust) ==True:
            return([adj])
            break

def density_mat_gen(nteams,density):
    den_mat=[]
    for i in range(0,nteams):
        den_mat.append([])
        for j in range(0,nteams):
            den_mat[i].append(density)
    return(den_mat)



def nteam_net_no_1(n,teamsizes,densities):
    #teamsizes is a list having all the teamsizes
    #n is the number of teams



    if len(teamsizes)!=n or len(densities)!=n:
        raise ValueError
    
    trange=team_ranges(teamsizes)

    num_nodes=0
    for i in teamsizes:
        num_nodes+=i
    
    
    edge_mat=[]
    
    for i in range(0,n):
        edge_mat.append([])
        for j in range(0,n):
            edge_mat[i].append(np.floor(densities[i][j]*teamsizes[i]*teamsizes[j]))
    
    edge_mat_exhaust=copy.deepcopy(edge_mat)


    adjedge=[0 for i in range(0,num_nodes)]
    adj=[adjedge.copy() for i in range(0,num_nodes)]
    
    if edge_exhaust(edge_mat_exhaust)==True:
        return([adj])
    while edge_exhaust(edge_mat_exhaust)==False:
        i = random.randint(0,num_nodes-1)
        j = random.randint(0,num_nodes-1)
        data_edge=edge_sign_teams(trange,i,j)
        
        
        if data_edge[0]==1:
            edge_sign=0
        else:
            edge_sign=data_edge[0]
        
        l=data_edge[1]
        m=data_edge[2]
        
        
        if edge_mat_exhaust[l][m]!=0 and adj[i][j]==0:
            adj[i][j]=edge_sign
            edge_mat_exhaust[l][m]+=-1
    #We construct a nxn matrix having different number of different types of edges. 
        if edge_exhaust(edge_mat_exhaust) ==True:
            return([adj])
            break
