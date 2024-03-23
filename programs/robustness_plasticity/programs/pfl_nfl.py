import networkx as nx
import pandas as pd
import numpy as np
import parse
import os 
import glob

topofiles_path= glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/robustness_plasticity/programs/Gene_Network_Modelling-master/topofiles/*topo")
topofiles=[x.split("/")[-1] for x in topofiles_path]

os.chdir("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/robustness_plasticity/programs/Gene_Network_Modelling-master/topofiles")
file=topofiles[11]

print(file)
adj=parse.adj_extract(file)

adj=np.matrix(adj)
print(adj)
graph=nx.from_numpy_array(adj)


def pfl_nfl_calc(adj):
    adj=np.matrix(adj)
    graph=nx.from_numpy_array(adj)
    cycles=nx.simple_cycles(graph)
    pos=0
    neg=0
    for i in cycles:
        sum=1
        cycle_length=len(i)
        for j in range(0,cycle_length):
            if j<cycle_length-1:
                sum*= graph.edges[i[j],i[j+1]]["weight"]
                
            elif j==cycle_length-1:
                sum*= graph.edges[i[j], i[0]]["weight"]
        if sum>0:
            pos+=1
        elif sum<0:
            neg+=1
    return(pos,neg)
print(pfl_nfl_calc(adj))