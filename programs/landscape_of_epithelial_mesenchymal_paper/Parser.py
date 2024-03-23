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

def node_summary(filename):
    tdata=pd.read_csv("{}".format(filename), sep =" ")
    list_of_nodes=node_list_generator(filename)
    n=len(list_of_nodes)
    out_in=[]
    for i in range(0,n):
        out_in.append([0,0])
    for i in tdata.values:
        out_index=list_of_nodes.index(i[0])
        in_index=list_of_nodes.index(i[1])
        out_in[out_index][0]+=1
        out_in[in_index][1]+=1
    core_nodes=[]
    for i in range(0,n):
        if (out_in[i][0]!=0 and out_in[i][1]!=0):
            core_nodes.append(list_of_nodes[i])
    
    
    n2=len(core_nodes)
    out_in2=[]

    def ind2(i):
        return(core_nodes.index(i))
    for i in range(0,n2):
        out_in2.append([0,0])
    
    for i in tdata.values:
        if i[0] in core_nodes and i[1] in core_nodes:
            out_in2[ind2(i[0])][0]+=1
            out_in2[ind2(i[1])][1]+=1
    core_nodes_2=[]
    for i in range(0,n2):
        if (out_in2[i][0]!=0 and out_in2[i][1]!=0):
            core_nodes_2.append(core_nodes[i])
    return(core_nodes_2)

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
        
def adj_update(nodes_list,filename):

    topo_data=pd.read_csv("{}".format(filename), sep =" ")
    topo_ids=nodes_list
    
    def ind(i):
        return(topo_ids.index(i))

    n=len(topo_ids)

    adj=[]
    for i in range(n):
        adj.append(np.zeros(n))

    
    for i in topo_data.values:
        if i[0] in topo_ids and i[1] in topo_ids:                
            if i[2]==1:
                adj[ind(i[0])][ind(i[1])] = 1
            if i[2]==2:
                adj[ind(i[0])][ind(i[1])]= -1
    return(adj)

def adj_extract_core(filename):
    nodes=node_summary(filename)
    k=adj_update(nodes,filename)
    return(k)


def topofile_summary_core(file):
    adj=adj_extract_core(file)
    n=len(adj)
    edges=0
    pedges=0
    nedges=0
    for i in adj:
        for j in i:
            if j!=0:
                edges+=1
                if j==-1:
                    nedges+=1
                elif j==+1:
                    pedges+=1
    return(n,edges,pedges,nedges,file)

topofiles_path= glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/landscape_of_epithelial_mesenchymal_paper/teams_data/Teams-main/TopoFiles/*topo")
topofiles=[x.split("/")[-1] for x in topofiles_path]

def network_summary(adj):
    n=len(adj)
    edges=0
    pedges=0
    nedges=0
    for i in adj:
        for j in i:
            if j!=0:
                edges+=1
                if j==-1:
                    nedges+=1
                elif j==+1:
                    pedges+=1
    return(n,edges,pedges,nedges)


    
#print(adj_extract_core(topofiles[0]))


#print(node_summary(topofiles[2]))
