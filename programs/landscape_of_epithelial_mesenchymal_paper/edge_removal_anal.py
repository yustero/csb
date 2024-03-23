import numpy as np
import pandas as pd
import glob
import os
import Parser
import boolean_sim
import randomization
import copy
import team_influence
import random

def more_team(no_of_updates,file):
    adj=Parser.adj_extract_core(file)
    n=len(adj)
    team_strengths=[]
    can=[]
    cluster=team_influence.clustering(adj)
    adj2=team_influence.updated_matrix_from_adj(adj,file)
    updated_adj=copy.deepcopy(adj2)
    
    wt_inf= team_influence.influence_matrix(updated_adj)
    wt_ts= team_influence.team_strength(wt_inf,cluster,updated_adj)
    wt_can=boolean_sim.canal_node(updated_adj)

    can.append(wt_can)
    team_strengths.append(wt_ts)
    i=0
    while i< no_of_updates:
        
        upinf=team_influence.influence_matrix(updated_adj)
        uts=team_influence.team_strength(upinf,cluster,updated_adj)
        temp_adj=copy.deepcopy(updated_adj)
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
        c=random.randint(0,n-1)
        d=random.randint(0,n-1)
        if updated_adj[a][b]*updated_adj[c][d]==-1:
            i+=1
            buffer= temp_adj[c][d]  
            temp_adj[c][d]=  temp_adj[a][b]
            temp_adj[a][b] = buffer

        
            
            temp_inf=team_influence.influence_matrix(temp_adj)
            temp_ts=team_influence.team_strength(temp_inf,cluster, updated_adj)
            
            
                        
            if temp_ts> uts:
                updated_adj=temp_adj
                ucan=boolean_sim.canal_node(temp_adj)
                can.append(ucan)
                team_strengths.append(temp_ts)
                print(temp_ts,uts)
    return(team_strengths,can)

topofiles_path= glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/landscape_of_epithelial_mesenchymal_paper/teams_data/Teams-main/TopoFiles/*topo")
topofiles=[x.split("/")[-1] for x in topofiles_path]
file = topofiles[0]
print(file)
print(more_team(1000, file))