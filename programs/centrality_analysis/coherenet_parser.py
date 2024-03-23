import os 
import glob
import numpy as np 
import copy 
import pandas as pd
from scipy.cluster import hierarchy as hi 


path1="/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/centrality_analysis/topofiles"

os.chdir(path1)



def node_list(filename):
    data=pd.read_csv("{}".format(filename), sep = " ")
    list_of_nodes=[]
    n = len(list(data["Source"]))
    for i in range(0,n):
        
        if list(data.loc[i,"Source":"Target"]) [0] not in list_of_nodes:
            list_of_nodes.append(list(data.loc[i,"Source":"Target"]) [0])

        if list(data.loc[i,"Source":"Target"]) [1] not in list_of_nodes:
            list_of_nodes.append(list(data.loc[i,"Source":"Target"]) [1])
    return(list_of_nodes)

def adj_per(filename):
    nodes=node_list(filename)
    data=pd.read_csv(filename, sep =" ")
    n=len(nodes)
    adj=[]
    for i in range(0,n):
        adj.append([0 for i in range(0,n)])
    
    def ind(node):
        return(nodes.index(node))

    for i in data.values:
        if i[2]==1:
            adj[ind(i[0])][ind(i[1])]=1
        if i[2]==2:
            adj[ind(i[0])][ind(i[1])]=-1
    return(adj, nodes)

def adj_nodes(filename,nodes):
    
    data=pd.read_csv(filename, sep =" ")
    n=len(nodes)
    adj=[]
    for i in range(0,n):
        adj.append([0 for i in range(0,n)])
    
    def ind(node):
        return(nodes.index(node))

    for i in data.values:
        if i[0] in nodes and i[1] in nodes:
            if i[2]==1:
                adj[ind(i[0])][ind(i[1])]=1
                
            if i[2]==2:
                adj[ind(i[0])][ind(i[1])]=-1
    return(adj, nodes)

def adj_peril(filename):
    dat=adj_per(filename)
    adj=dat[0]
    nodes=dat[1]
    upnode=nodes.copy()
    def in_outdegree_dist(adj):
        n=len(adj)
        indist=[]
        outdist=[]    
        for i in range(0,n):
            indeg=0
            outdeg=0
            for j in range(0,n):
                if adj[j][i]!=0:
                    indeg+=1
                if adj[i][j]!=0:
                    outdeg+=1
            indist.append(indeg)
            outdist.append(outdeg)
        return(indist,outdist)
    indist=in_outdegree_dist(adj)[0]
    outdist=in_outdegree_dist(adj)[1]
    
    n=len(indist)
    per_n=[]
    for i in range(0,n):
        if indist[i]==0 or outdist[i]==0:
            upnode.remove(nodes[i])
    
    dat=adj_nodes(filename,upnode)
    adj=dat[0]
    nodes=dat[1]
    upnode=nodes.copy()
    
    indist=in_outdegree_dist(adj)[0]
    outdist=in_outdegree_dist(adj)[1]
    
    n=len(indist)
    for i in range(0,n):
        if indist[i]==0 or outdist[i]==0:
            upnode.remove(nodes[i])

    adj=adj_nodes(filename,upnode)[0]
    
    return(adj,upnode)

def adj_peril_in(filename):
    dat=adj_per(filename)
    adj=dat[0]
    nodes=dat[1]
    upnode=nodes.copy()
    def in_outdegree_dist(adj):
        n=len(adj)
        indist=[]
          
        for i in range(0,n):
            indeg=0
            
            for j in range(0,n):
                if adj[j][i]!=0:
                    indeg+=1
            
            indist.append(indeg)
            
        return(indist)
    indist=in_outdegree_dist(adj)
    print(indist)
    n=len(indist)
    per_n=[]
    for i in range(0,n):
        if indist[i]==0:
            upnode.remove(nodes[i])
    
    dat=adj_nodes(filename,upnode)
    adj=dat[0]
    nodes=dat[1]
    upnode=nodes.copy()
    indist=in_outdegree_dist(adj)
    print(indist)
    n=len(indist)
    for i in range(0,n):
        if indist[i]==0:
            upnode.remove(nodes[i])

    adj=adj_nodes(filename,upnode)[0]
    
    return(adj,upnode)

def influence_matrix(adj):
    inf= np.array(adj.copy())
    almax=np.array(adj.copy())
    almax[almax!=0]=1
    
    for i in range(2,11):
        infl=np.linalg.matrix_power(adj,i).astype(float)
        alamxp=np.linalg.matrix_power(almax,i).astype(float)
        inf = inf + np.divide(infl, alamxp, out= np.zeros_like(infl), where = alamxp!=0)
    inf=inf/10
    cinf=inf.copy()
    return(cinf)

def clustering(adj):
    inf=influence_matrix(adj).copy()
    d=hi.distance.pdist(inf)
    l=hi.linkage(d, method='complete')
    clust=hi.cut_tree(l, n_clusters=2)
    
    cluster=np.transpose(clust).copy()
    return(cluster)

def clustered_matrix_file(filename):
    dat=adj_peril(filename)
    adj=dat[0]
    nodes=dat[1]
    n=len(nodes)

    clust=clustering(adj)[0]
    t1=[]
    t2=[]    
    for i in range(0,n):
        if clust[i]==0:
            t1.append(nodes[i]) 

        if clust[i] ==1:
            t2.append(nodes[i])
    tot=t1+t2
    
    adj=adj_nodes(filename,tot)[0]

    return(adj,t1,t2,tot)

def clustered_matrix_adj(adj):
    clust=clustering(adj)[0]
    n=len(adj)
    t1=[]
    t2=[]
    for i in range(0,n):
        if clust[i]==0:
            t1.append(i)
        elif clust[i]==1:
            t2.append(i)
    tot=t1+t2
    adj2=[]
    for i in range(0,n):
        edge=[]
        for j in range(0,n):
            edge.append(adj[tot[i]][tot[j]])
        adj2.append(edge)
    return(adj2,len(t1),len(t2))

def team_strength_file(adj):
    clustered_data=clustering(adj)
    influenced_matrix=influence_matrix(adj)
    n=len(adj)
    counter=0
    for i in range(0,n):
        if clustered_data[0][i]==0:
            counter+=1
    a=counter
    b=n-counter
    ts1,ts2,ts3,ts4=0,0,0,0
    for i in range(0,a):
        for j in range(0,a):
            ts1+=influenced_matrix[i][j]
    for i in range(a,n):
        for j in range(a,n):
            ts2+=influenced_matrix[i][j]
    for i in range(0,a):
        for j in range(a,n):
            ts3+=influenced_matrix[i][j]
    for i in range(a,n):
        for j in range(0,a):
            ts4+=influenced_matrix[i][j]

    ts1=abs(ts1/(a*a))
    ts2=abs(ts2/(b*b))
    ts3=abs(ts3/(a*b))
    ts4=abs(ts4/(a*b))
    team_strength=(ts1+ts2+ts3+ts4)/4
    return(team_strength)

def team_strength_rand(adj,clustered_data):
    influenced_matrix=influence_matrix(adj)
    n=len(adj)
    counter=0
    for i in range(0,n):
        if clustered_data[0][i]==0:
            counter+=1
    a=counter
    b=n-counter
    ts1,ts2,ts3,ts4=0,0,0,0
    for i in range(0,a):
        for j in range(0,a):
            ts1+=influenced_matrix[i][j]
    for i in range(a,n):
        for j in range(a,n):
            ts2+=influenced_matrix[i][j]
    for i in range(0,a):
        for j in range(a,n):
            ts3+=influenced_matrix[i][j]
    for i in range(a,n):
        for j in range(0,a):
            ts4+=influenced_matrix[i][j]

    ts1=abs(ts1/(a*a))
    ts2=abs(ts2/(b*b))
    ts3=abs(ts3/(a*b))
    ts4=abs(ts4/(a*b))
    team_strength=(ts1+ts2+ts3+ts4)/4
    return(team_strength)


def rand_team_strength_rand(adj,a,b):
    influenced_matrix=influence_matrix(adj)
    n=len(adj)
    ts1,ts2,ts3,ts4=0,0,0,0
    for i in range(0,a):
        for j in range(0,a):
            ts1+=influenced_matrix[i][j]
    for i in range(a,n):
        for j in range(a,n):
            ts2+=influenced_matrix[i][j]
    for i in range(0,a):
        for j in range(a,n):
            ts3+=influenced_matrix[i][j]
    for i in range(a,n):
        for j in range(0,a):
            ts4+=influenced_matrix[i][j]

    ts1=abs(ts1/(a*a))
    ts2=abs(ts2/(b*b))
    ts3=abs(ts3/(a*b))
    ts4=abs(ts4/(a*b))
    team_strength=(ts1+ts2+ts3+ts4)/4
    return(team_strength)

path1="/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/centrality_analysis/topofiles"
filedat=glob.glob(path1+"/*topo")
topofiles=[x.split("/")[-1] for x in filedat]
nodes=node_list(topofiles[2])
