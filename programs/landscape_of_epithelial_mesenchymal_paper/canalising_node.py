import boolean_sim
import Parser
import team_influence
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import glob
import randomization
import os






topofiles_path= glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/landscape_of_epithelial_mesenchymal_paper/teams_data/Teams-main/TopoFiles/*topo")
topofiles_2_path=glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/robustness_plasticity/programs/Gene_Network_Modelling-master/topofiles/*topo")
topofiles=[x.split("/")[-1] for x in topofiles_path]

topofiles2= [x.split("/")[-1] for x in topofiles_2_path]

#os.chdir("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/robustness_plasticity/programs/Gene_Network_Modelling-master/topofiles")







def histogram_gen(list,number):
    max = np.max(list)+1
    min = np.min(list)
    rge=np.linspace(min,max, number)
    hist=[]
    for i in range(0,number-1):
        counter=0
        for j in list:
            if j>= rge[i] and j<rge[i+1]:
                counter+=1
        hist.append(counter)
    hist.append(0)

    return(rge,hist)


def distribution(file,number):


    adj_initial=Parser.adj_extract_core(file)
    adj1=team_influence.updated_matrix_from_adj(adj_initial,file)
    

    
    cluster1=team_influence.clustering(adj_initial)
    #team strength for wt network    
    influence1=team_influence.influence_matrix(adj1)
    teamss1=team_influence.team_strength(influence1,cluster1,adj1)

    #canal distribution for null network

    cans1= boolean_sim.canal_node_summary(adj1)

    
    high_teams=[]
    low_teams=[]

    for i in range(0,number):
        
        #rand_mat=randomization.random_edge_exchange(adj1,4).copy()
        #rand_mat=randomization.edge_deletions(adj1,2)
        rand_mat=randomization.edge_inversion(adj1,2)
        
        
        cluster=cluster1
        clust_mat=team_influence.clustered_matrix(rand_mat,cluster)
        influence=team_influence.influence_matrix(clust_mat)
        teamss=team_influence.team_strength(influence,cluster,rand_mat)

        if teamss>teamss1:
            cans=boolean_sim.canal_node_summary(rand_mat)
            high_teams.append([teamss,cans])

        elif teamss<teamss1:
            cans=boolean_sim.canal_node_summary(rand_mat)
            low_teams.append([teamss,cans])

    
    ltn=len(low_teams)
    for i in range(0,ltn):
        pass
        #plt.scatter(low_teams[i][1][2], low_teams[i][1][1], color="green")
    htn=len(high_teams)
    
    for i in range(0,htn):
        pass
        #plt.scatter( high_teams[i][1][2], high_teams[i][1][1], color="blue")
    
    #plt.scatter( cans1[2], cans1[1], color="red")
    #plt.show()
    print(cans1[0])
    plt.hist(cans1[0],alpha=0.5,label="{}_{}_wt".format(teamss1,file))
    #plt.hist(high_teams[0][1][0],alpha=0.25, label="high_ts_{}_rn_{}".format(high_teams[0][0],file))
    #plt.hist(low_teams[0][1][0],alpha=0.25, label="low_ts_{}_rn_{}".format(low_teams[0][0],file))
    
    plt.legend(loc='upper right')
    plt.show()
'''    i=0
    j=0
    wt_data=histogram_gen(cans1[0],10)
    plt.plot(wt_data[0],wt_data[1], color="blue", marker="o")
    high_team_data=histogram_gen(high_teams[i][1][0],10)
    plt.plot(high_team_data[0],high_team_data[1], color="red", marker = "o")
    low_team_data=histogram_gen(low_teams[j][1][0],10)

'''

#i=7
#print(topofiles[i])
#distribution(topofiles[i],1000)

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
def pos_neg(li):
    
    positive=[]
    negative=[]
    for i in li:
        positive.append(i[0])
        negative.append(i[1])
    return(positive,negative)

def indx(li):
    n=len(li)
    ind=[]
    for i in range(1,n+1):
        ind.append(i)
    return(ind)
# for topofile2 i.e emt racipe network removing the node with cal value = 9 removed hybrid states? that's funny

file=topofiles[2]
print(file)
adj_initial=Parser.adj_extract_core(file)
adj1=team_influence.updated_matrix_from_adj(adj_initial,file)

adj2=adj1
adj2=remove_nodes_num(adj1,[1])
print(boolean_sim.canal_node_summary(adj2)[0], "before change")
print( "in posneg", boolean_sim.outgoing_node(adj2)[-1])
ind=indx(adj2)
out_pos=pos_neg(boolean_sim.canal_node_summary(adj2)[-1])[0]

out_neg=pos_neg(boolean_sim.canal_node_summary(adj2)[-1])[1]

#plt.scatter(ind,[out_neg[i]-out_pos[i] for i in range(len(out_neg))], color ="r")
#plt.scatter(ind,out_pos, color="g")
#plt.show()

#9, 14
#10,12,13
#print( boolean_sim.canal_node_summary(adj2)[0],"after change")
print("posneg", boolean_sim.canal_node_summary(adj1)[-1])
steadys1=boolean_sim.steady_states(adj1,1000)


k2=boolean_sim.steady_state_frequency(steadys1,adj1)
steadys=boolean_sim.steady_states(adj2,1000)


k=boolean_sim.steady_state_frequency(steadys,adj2)
print(hamming_distance(k))
boolean_sim.bar_graph(k,"hello")

