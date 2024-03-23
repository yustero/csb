import networkx as nx
import coherent_parser
import numpy as np 
import topopath
import random 
import node_metrics
import matplotlib.pyplot as plt
import randomization
import boolean_siml

def path_legth_plot(adj):
    n=len(adj)
    indli=[x for x in range(0,n)]
    adj2=np.matrix(adj)
    graph=nx.from_numpy_array(adj2)
    plwt=nx.average_shortest_path_length(graph)
    
    path_dist=[]
    
    
    for i in range(0,n):
        pathl=0
        count=0
        for j in range(0,1000):
            nodes=random.sample(indli,i)
            mat= node_metrics.node_knockout(adj,nodes)
            
            mat=np.matrix(mat)
            if len(mat)>0:
                graph_temp=nx.from_numpy_array(mat)
                if nx.is_connected(graph_temp):
                    pathl+=nx.average_shortest_path_length(graph_temp)
                    count+=1
            else:
                count+=1
        path_dist.append(pathl/count)
    return(path_dist,indli)


adj=coherent_parser.clustered_matrix_file(topopath.topofiles[4])[0]
adj2=np.matrix(adj)
graph=nx.from_numpy_array(adj2)

nodec=[]
nodec.append(nx.node_connectivity(graph))
print(nodec)
for i in range(0,1000):

    rmat=randomization.edge_change(adj,10)
    radj=np.matrix(rmat)
    graph2=nx.from_numpy_array(radj)
    nodec.append(nx.node_connectivity(graph2))
print(nodec[0], np.mean(nodec))

'''n=len(adj)
indli=[x for x in range(0,n)]
for i in range(0,n):
    for j in range(0,10):
        nodes=random.sample(indli,i+1)  
        mat= node_metrics.node_knockout(adj,nodes)
        mat=np.matrix(mat)
        print(mat)
        graph_temp=nx.from_numpy_array(mat)
        pathl=nx.average_shortest_path_length(graph_temp)
        print(pathl)
   '''         