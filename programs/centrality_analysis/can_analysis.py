import boolean_sim
import coherenet_parser
import randomization
import random
import node_metrics
import matplotlib.pyplot as plt
import copy
import numpy as np
import glob
mat=randomization.random_matrix_generator(200)


def small_world(adj,num,p):
    mat=copy.deepcopy(adj)
    n=len(adj)
    for i in range(0,num):
        if random.random()<p:
            a=random.randint(0,n-1)
            b=random.randint(0,n-1)
            c=random.randint(0,n-1)
            d=random.randint(0,n-1)
            buffer= mat[c][d]  
            mat[c][d]=  mat[a][b]
            mat[a][b] = buffer
    return(mat)

path1="/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/centrality_analysis/topofiles"
filedat=glob.glob(path1+"/*topo")
topofiles=[x.split("/")[-1] for x in filedat]


adj1=coherenet_parser.clustered_matrix_file(topofiles[2])[0]
cluster=coherenet_parser.clustering(adj1)

ts1=coherenet_parser.team_strength_rand(adj1,cluster)
mean_time=[]
team_strength=[]
lsol=[]

#mtime=boolean_sim.steady_states_time(adj1,1000)[-1]
#mean_time.append(mtime)

steadys1=boolean_sim.steady_states(adj1,1000)
ssf1=boolean_sim.steady_state_frequency(steadys1, adj1)
lsol1=boolean_sim.long_cycles(ssf1)

team_strength.append(team_strength)
lsol.append(lsol1)
print(ts1,lsol1)

for i in range(0,100):
    adj=copy.deepcopy(adj1)
    mat=randomization.random_edge_exchange(adj,2)
    #ts=coherenet_parser.team_strength_rand(mat,cluster)
    dat=  coherenet_parser.clustered_matrix_adj(mat)
    mat=dat[0]
    a=dat[1]
    b=dat[2]
    ts=coherenet_parser.rand_team_strength_rand(mat,a,b)
    team_strength.append(ts)

    stead=boolean_sim.steady_states(mat,1000)
    ssfr=boolean_sim.steady_state_frequency(stead,mat)
    lsolr=boolean_sim.long_cycles(ssfr)
    lsol.append(lsolr)
    print(lsolr,ts)


    #mt=boolean_sim.steady_states_time(mat,1000)[-1]    
    #print(mt,ts)
    #mean_time.append(mt)
    
    
    
    
plt.scatter(team_strength,lsol)
plt.xlabel("Team strength")
plt.ylabel("Number of late solutions")
plt.scatter(ts1,lsol1, color="r")

plt.show()