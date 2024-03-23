import Parser
import randomization
import node_metrics
import boolean_sim
import team_influence
import matplotlib.pyplot as plt
import numpy as np
import os
import glob


def remove_nodes(adj,z):
    n=len(adj)
    cdist=boolean_sim.canal_node_summary(adj)[0]
    print(cdist)
    mat=[]
    for i in range(0,n):
        edge=[]
        

        if cdist[i]!=z:
            for j in range(0,n):
                if cdist[j]!=z:
                    edge.append(adj[i][j])
            mat.append(edge)
    return(mat)

def remove_nodes_num(adj,z):
    n=len(adj)
    mat=[]
    for i in range(0,n):
        edge=[]
        

        if i not in z:
            for j in range(0,n):
                if j not in z:
                    edge.append(adj[i][j])
            mat.append(edge)
    return(mat)

def two_largest(inlist):
    largest=0
    second_largest=0
    for item in inlist:
        if item > largest:
            largest = item
        elif largest > item > second_largest:
            second_largest = item
    # Return the results as a tuple
    return largest, second_largest

def hamming(li1,li2):
    ham=0
    n=len(li1)
    for i in range(0,n):
        if li1[i]!=li2[i]:
            ham+=1
    return(ham)
def hamming_distance(ssf):
    large=two_largest(ssf[1])[0]
    slarge=two_largest(ssf[1])[1]
    largei=ssf[1].index(large)
    slargi=ssf[1].index(slarge)
    ham_dis=[]
    for i in ssf[0]:
        ham_dis.append(min(hamming(i,ssf[0][largei]),hamming(i,ssf[0][slargi]) ))
    return(ham_dis)


path1="/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/centrality_analysis/topofiles"
filedat=glob.glob(path1+"/*topo")
topofiles=[x.split("/")[-1] for x in filedat]
print(topofiles)



file=topofiles[2]
adj_initial=Parser.adj_extract_core(file)
adj1=team_influence.updated_matrix_from_adj(adj_initial,file)

indx=[i for i in range(len(adj1))]

adj1s= node_metrics.adj_summary(adj1)
indeg = node_metrics.indeg_summary(adj1)
outdeg = node_metrics.outdeg_summary(adj1)
ind = node_metrics.indegree(adj1)
outd = node_metrics.outdeg_summary(adj1)  


adj2=adj1
i=0
adj2=remove_nodes_num(adj1,[i])
print("positive :", outdeg[1][i],"negative: ", outdeg[2][i], "absolute difference (out):", outdeg[0][i])
print("positive :", indeg[1][i],"negative: ", indeg[2][i], "absolute difference (in):", indeg[0][i])

#steadys1=boolean_sim.steady_states(adj1,1000)


#k2=boolean_sim.steady_state_frequency(steadys1,adj1)
steadys=boolean_sim.steady_states(adj2,1000)


k=boolean_sim.steady_state_frequency(steadys,adj2)
ham = hamming_distance(k)
print(ham,len(ham))
boolean_sim.bar_graph(k,"hello")


'''
randmat=randomization.random_edge_exchange(adj2,10)
plt.hist(indeg[0], alpha=0.5)
plt.hist(node_metrics.indeg_summary(randmat)[0],alpha=0.5)
print(indeg[0])
plt.show()
plt.savefig("emtracipe_indeg_distribution_relaxed.jpg")'''