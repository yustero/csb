import pandas as pd 
import numpy as np 
import subprocess
import glob
import os 
from multiprocessing import Pool 
from scipy.cluster import hierarchy as hi 
import matplotlib.pyplot as plt
import seaborn as sns
import Parser
import boolean_sim
import randomization

topofiles_path= glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/landscape_of_epithelial_mesenchymal_paper/teams_data/Teams-main/TopoFiles/*topo")
topofiles=[x.split("/")[-1] for x in topofiles_path]



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

def new_influence(adj):
    infn = np.array(adj.copy())
    M_max = np.array(adj.copy())
    M_max[M_max != 0] = 1.0
    for i in range(2,101):
            a = np.linalg.matrix_power(adj,i).astype(float)
            b = np.linalg.matrix_power(M_max,i).astype(float)
            infn = infn + np.divide(a, b, out = np.zeros_like(a), where=b!=0)/(i)

    infn = infn/sum(np.reciprocal(np.arange(1, 101), dtype=float))
    return(infn)

def clustering(adj):
    inf=influence_matrix(adj).copy()
    d=hi.distance.pdist(inf)
    l=hi.linkage(d, method='complete')
    clust=hi.cut_tree(l, n_clusters=2)
    
    cluster=np.transpose(clust).copy()
    return(cluster)

def updated_node_list(clustered_data,adj,file):
    n=len(adj)
    clust1=[]
    clust2=[]
    for i in range(0,n):
        if clustered_data[0][i]==0:
            clust1.append(i)
        if clustered_data[0][i]==1:
            clust2.append(i)
    nodes=Parser.node_summary(file)
    new_nodes=[]
    
    indexes=clust1+clust2
    
    for i in indexes:
        new_nodes.append(nodes[i])
    return(new_nodes)

def updated_matrix_from_adj(adj,file):
    cluster=clustering(adj)
    upnode=updated_node_list(cluster,adj,file)
    updated_matrix=Parser.adj_update(upnode,file)    
    return(updated_matrix)

def team_strength(influenced_matrix, clustered_data,adj):
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
    
def clustered_matrix(adj,cluster):
    n=len(adj)
    clustered_adj=[]
    for i in range(0,n):
        clustered_adj.append(np.zeros(n))
    indexes=[]
    for i in range(0,n):
        if cluster[0][i]==0:
            indexes.append(i)
        if cluster[0][i]==1:
            indexes.append(i)
    for i in range(0,n):
        for j in range(0,n):
            clustered_adj[i][j]=adj[indexes[i]][indexes[j]]
    return(clustered_adj)

'''file=topofiles[1]
adj=Parser.adj_extract_core(file)
m= clustering(adj)

z=updated_node_list(m,adj,file)


kk=Parser.adj_update(z,file)           
    
infl2= influence_matrix(kk)
rand_mat=randomization.random_edge_exchange(kk,10)
cls=clustering(rand_mat)
#print(kk)

#print(clustered_matrix(rand_mat,cls))

def influence_2(adj):
    inf = np.array(adj.copy())
    M_max = adj.copy()
    M_max[M_max != 0] = 1.0
    for i in range(2,11):
            a = np.linalg.matrix_power(adj, i).astype(float)
            b = np.linalg.matrix_power(M_max, i).astype(float)
            inf = inf + np.divide(a, b, out=np.zeros_like(a), where=b!=0)

    inf = inf/10
    return(inf)

adj=Parser.adj_extract_core(file)
m= clustering(adj)

z=updated_node_list(m,adj,file)


kk=Parser.adj_update(z,file)
print(team_strength_from_matrix(kk))
#for i in influence_matrix(kk):
#    print(i)

print("-------")
#infl1= influence_matrix(adj)
infl2= influence_matrix(kk)
print(team_strength(infl2,m,kk))
print(len(kk))
#for i in influence_matrix(adj):
#    print(i)


#ax = sns.heatmap(infl2, linewidth=0.5)
#ax=sns.heatmap(infl1, linewidth=0.5)

#plt.show()

#print(adj)
print(randomization.random_edge_exchange(kk,10))

'''