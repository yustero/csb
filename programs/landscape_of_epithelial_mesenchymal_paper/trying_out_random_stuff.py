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

os.chdir("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/robustness_plasticity/programs/Gene_Network_Modelling-master/topofiles")
print(topofiles2)

#0
'''adj_initial=Parser.adj_extract_core(file)
adj1=team_influence.updated_matrix_from_adj(adj_initial,file)
cluster1=team_influence.clustering(adj_initial)
influence1=team_influence.influence_matrix(adj1)
teamss1=team_influence.team_strength(influence1,cluster1,adj1)
'''
#print(boolean_sim.canal_node(adj1))

def team_length(clustering):
    a=0
    b=0
    for i in clustering[0]:
        if i==0:
            a+=1
        elif i==1:
            b+=1
    return(a,b)
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

    
def team_strength_vs_canal(number,file):
    teams=[]
    can=[]
    posm=[]
    var=[]
    var_mean=[]
    adj_initial=Parser.adj_extract_core(file)
    adj1=team_influence.updated_matrix_from_adj(adj_initial,file)
    cluster1=team_influence.clustering(adj_initial)
    print(cluster1)
    influence1=team_influence.influence_matrix(adj1)
    teamss1=team_influence.team_strength(influence1,cluster1,adj1)
    teams.append(teamss1)

    
    mcan1=boolean_sim.canal_node(adj1)
    can.append(mcan1)
    var1= boolean_sim.canal_node_summary(adj1)[1]
    var.append(var1)
    
    varm1=var1/mcan1
    var_mean.append(varm1)
    #pos=boolean_sim.pfl_nfl_calc(adj1)
    #posm.append(pos)
    
    print(teams,mcan1, var1)
   

    for i in range(0,number):
        
        rand_mat=randomization.random_edge_exchange(adj1,10).copy()
        #rand_mat=randomization.edge_deletions(adj1,10)
        #rand_mat=randomization.edge_inversion(adj1,2)
        #cluster=team_influence.clustering(rand_mat)
        cluster=cluster1
        
        clust_mat=team_influence.clustered_matrix(rand_mat,cluster)
        influence=team_influence.influence_matrix(clust_mat)

        teamss=team_influence.team_strength(influence,cluster,rand_mat)
        
        mcan=boolean_sim.canal_node(rand_mat)
        can.append(mcan)
        var2=boolean_sim.canal_node_summary(rand_mat)[1]
        teams.append(teamss)
        var.append(var2)

        varm2=var2/mcan
        var_mean.append(varm2)
        #pos1=boolean_sim.pfl_nfl_calc(rand_mat)
        #posm.append(pos1)
        #print(teamss,canl,mcan)
        
        
    print(file)
    #teams vs can
    '''plt.scatter(teams,can)
    plt.scatter(teamss1,mcan1, c="r")
    plt.ylabel("mean_robustness_of_a_single_node")
    plt.xlabel("teamstrength")'''

    #plt.savefig("{}_teams_vs_can".format(file))
    
    #can vs var
    
    '''plt.scatter(can,var)
    plt.scatter(mcan1,var1, c="r")
    plt.ylabel("variance")
    plt.xlabel("mean_robustness_of_a_single_node")'''
    #plt.savefig("{}_variance_vs_can.jpg".format(file))

    
    plt.hist(can, bins=40, color="c", label="{}".format(file))
    plt.axvline(mcan1, color='r', linestyle='dashed', linewidth=1)
    plt.xlabel("mean_canalizing_strength")
    plt.ylabel("Frequency")
    plt.legend(loc='upper right')

    print(mcan1)

    #var vs teams
    '''plt.scatter(teams,var)
    plt.scatter(teamss1,var1, c="r")
    plt.ylabel("variance")
    plt.xlabel("teamstrength")

    plt.savefig("{}_variance_vs_teamstrength.jpg".format(file))
    '''
    #var/mean vs teams
    '''plt.scatter(teams,var_mean)
    plt.scatter(teamss1,varm1, c="r")
    plt.show()'''
    #plt.savefig("{}_variance_by_mean_vs_team_strength.jpg".format(file))
    

    
    
    
    
    plt.show()
    print("job done boss")

    '''fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(teams,can ,var ,
           linewidths=1, alpha=.7,
           edgecolor='k',
           s = 2,
           c="b")
    ax.scatter(teamss1,mcan1,var1,c="r")
    plt.show()'''

    return(teams,can)   
print(topofiles)
file=topofiles[0]
team_strength_vs_canal(1000,file)
#for file in topofiles:
#    team_strength_vs_canal(1000,file)