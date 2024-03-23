import matplotlib.pyplot as plt 
import boolean_sim
import Parser
import team_influence
import randomization
import numpy as np
import pandas as pd
import glob

topofiles_path= glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/landscape_of_epithelial_mesenchymal_paper/teams_data/Teams-main/TopoFiles/*topo")
topofiles=[x.split("/")[-1] for x in topofiles_path]





def team_strength_vs_steady_states(number,file):
    teams=[]
    number_of_steady_states=[]
    bimodal=[]
    adj_initial=Parser.adj_extract_core(file)
    adj1=team_influence.updated_matrix_from_adj(adj_initial,file)
    cluster1=team_influence.clustering(adj_initial)
    influence1=team_influence.influence_matrix(adj1)
    teamss1=team_influence.team_strength(influence1,cluster1,adj1)
    teams.append(teamss1)
    
    
    ssf1=boolean_sim.steady_state_frequency(boolean_sim.steady_states(adj1,1000),adj1)
    nss1=len(ssf1[1])
    bimol1=boolean_sim.biomdality(ssf1,adj1)
    number_of_steady_states.append(nss1)
    bimodal.append(bimol1)
    print(bimodal,number_of_steady_states,teams)
    #out=[teams[0], number_of_steady_states[0],bimodal[0]]
    #df=pd.DataFrame([out], columns=["Team strength", "NSS", "Bimodality"])
    #df.to_csv("ts3.csv", index=False, sep=" ")

    for i in range(0,number):
        
        rand_mat=randomization.random_edge_exchange(adj1,10).copy()
        
        #cluster=team_influence.clustering(rand_mat)
        cluster=cluster1
        clust_mat=team_influence.clustered_matrix(rand_mat,cluster)
        influence=team_influence.influence_matrix(clust_mat)

        teamss=team_influence.team_strength(influence,cluster,rand_mat)
        

        teams.append(teamss)
        print(teamss)
        
        
        ssf=boolean_sim.steady_state_frequency(boolean_sim.steady_states(rand_mat,1000),adj1)
        nss=len(ssf[1])
        print(nss,".")
        
        number_of_steady_states.append(nss)
        bimol=boolean_sim.biomdality(ssf,adj1)
        print(teamss,nss,bimol, ".")
        bimodal.append(bimol)

        out=[teams[i+1],number_of_steady_states[i+1],bimodal[i+1]]
        df=pd.DataFrame([out])
        if bimodal[i+1]!=0:
            df.to_csv("ts3.csv",mode="a", index=False, header=False, sep=" ")
   
    #plt.scatter(teams,number_of_steady_states)
    #plt.show()
    
    return(teams,number_of_steady_states)
        
#print(team_strength_vs_steady_states(500,topofiles[2]))

#file=topofiles[1]

df =pd.read_csv("ts3.csv", sep=" ")

n=len(df.values)
ts2=[]
ss2=[]
for i in range(0,n):
    ts2.append(df.iloc[i][0])
    ss2.append(df.iloc[i][1])

a=np.linspace(0,1,100)
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(ts2, bins = a)
 
#plt.scatter(ts, ss2)
plt.show()