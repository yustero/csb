import pandas as pd
import numpy as np
import glob

def node_list_generator(filename):
    #data=pd.read_csv("{}{}".format(filename,".topo"), sep =" ")
    data=pd.read_csv("{}".format(filename), sep =" ")
    list_of_nodes=[]
    n = len(list(data["Source"]))
    for i in range(0,n):
        
        if list(data.loc[i,"Source":"Target"]) [0] not in list_of_nodes:
            list_of_nodes.append(list(data.loc[i,"Source":"Target"]) [0])

        if list(data.loc[i,"Source":"Target"]) [1] not in list_of_nodes:
            list_of_nodes.append(list(data.loc[i,"Source":"Target"]) [1])
    return(list_of_nodes)

def adj_extract(filename):
    #topo_data= pd.read_csv("{}.{}".format(filename,"topo"), sep=" ")
    topo_data=pd.read_csv("{}".format(filename), sep =" ")
    topo_ids=node_list_generator(filename)
    
    def ind(i):
        return(topo_ids.index(i))

    n=len(topo_ids)

    adj=[]
    for i in range(n):
        adj.append(np.zeros(n))

    
    for i in topo_data.values:
        
        if i[2]==1:
            adj[ind(i[0])][ind(i[1])] = 1
        if i[2]==2:
            adj[ind(i[0])][ind(i[1])]= -1
    return(adj)
