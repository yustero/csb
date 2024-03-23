import pandas as pd
import numpy as np 

def adj_extract(filename):
    topo_data= pd.read_csv("{}.{}".format(filename,"topo"), sep=" ")
    topo_ids=pd.read_csv("{}.{}".format(filename,"ids"), sep =" ")

    def ind(i):
        return(list(topo_ids["node"].values).index(i))

    n=len(topo_ids["node"])

    adj=[]
    for i in range(n):
        adj.append(np.zeros(n))

    



    for i in topo_data.values:
        
        if i[2]==1:
            adj[ind(i[0])][ind(i[1])] = 1
        if i[2]==2:
            adj[ind(i[0])][ind(i[1])]= -1
    return(adj)
        
